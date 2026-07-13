"""
tests/parser/test_inheritance.py
Phase 1B/1C: Verify inheritance references are correctly extracted with
ReferenceKind.Inheritance and that the caller_fqn is set to the child class name.
"""
import textwrap
import codelens_core


class TestPythonInheritance:
    """Python class inheritance detected via `class Foo(Bar):` argument_list."""

    def _parse(self, source: str):
        p = codelens_core.ASTParser()
        p.set_language("python")
        return p.analyze_file("dummy.py", source)

    def test_single_inheritance_detected(self):
        """class Child(Parent): -> should produce one Inheritance reference."""
        src = textwrap.dedent("""\
            class Parent:
                pass
            class Child(Parent):
                pass
        """)
        ctx = self._parse(src)
        inherit_refs = [r for r in ctx.references if r.kind == codelens_core.ReferenceKind.Inheritance]
        assert len(inherit_refs) >= 1
        ref = inherit_refs[0]
        assert ref.callee_fqn == "Parent"

    def test_inheritance_caller_is_child_class(self):
        """The caller_fqn of an Inheritance reference should be the child class, not <global>."""
        src = textwrap.dedent("""\
            class Base:
                pass
            class Derived(Base):
                pass
        """)
        ctx = self._parse(src)
        inherit_refs = [r for r in ctx.references if r.kind == codelens_core.ReferenceKind.Inheritance]
        assert any(r.caller_fqn == "Derived" and r.callee_fqn == "Base" for r in inherit_refs)

    def test_multiple_inheritance(self):
        """class Multi(A, B): -> should produce two Inheritance references."""
        src = textwrap.dedent("""\
            class A:
                pass
            class B:
                pass
            class Multi(A, B):
                pass
        """)
        ctx = self._parse(src)
        inherit_refs = [r for r in ctx.references if r.kind == codelens_core.ReferenceKind.Inheritance]
        callee_names = {r.callee_fqn for r in inherit_refs}
        assert "A" in callee_names
        assert "B" in callee_names

    def test_method_calls_are_still_call_kind(self):
        """Regular function calls inside a class should NOT be Inheritance."""
        src = textwrap.dedent("""\
            class Foo:
                def bar(self):
                    print("hello")
        """)
        ctx = self._parse(src)
        # All references should be Call kind (print is a call, not inheritance)
        inherit_refs = [r for r in ctx.references if r.kind == codelens_core.ReferenceKind.Inheritance]
        assert len(inherit_refs) == 0

    def test_no_inheritance_plain_class(self):
        """A class with no parent should produce 0 Inheritance references."""
        ctx = self._parse("class Standalone:\n    pass\n")
        inherit_refs = [r for r in ctx.references if r.kind == codelens_core.ReferenceKind.Inheritance]
        assert len(inherit_refs) == 0


class TestCppInheritance:
    """C++ class inheritance detected via `base_class_specifier`."""

    def _parse(self, source: str):
        p = codelens_core.ASTParser()
        p.set_language("cpp")
        return p.analyze_file("dummy.cpp", source)

    def test_public_inheritance(self):
        """class Derived : public Base { } -> one Inheritance reference."""
        src = textwrap.dedent("""\
            class Base {};
            class Derived : public Base {};
        """)
        ctx = self._parse(src)
        inherit_refs = [r for r in ctx.references if r.kind == codelens_core.ReferenceKind.Inheritance]
        assert len(inherit_refs) >= 1
        assert any(r.callee_fqn == "Base" for r in inherit_refs)

    def test_inheritance_caller_is_child_class(self):
        """The caller_fqn of an Inheritance reference should be the child class."""
        src = textwrap.dedent("""\
            class Animal {};
            class Dog : public Animal {};
        """)
        ctx = self._parse(src)
        inherit_refs = [r for r in ctx.references if r.kind == codelens_core.ReferenceKind.Inheritance]
        assert any(r.caller_fqn == "Dog" and r.callee_fqn == "Animal" for r in inherit_refs)

    def test_cpp_function_calls_remain_call_kind(self):
        """Normal function calls in C++ should not be classified as Inheritance."""
        src = "void foo() { }\nvoid bar() { foo(); }\n"
        ctx = self._parse(src)
        inherit_refs = [r for r in ctx.references if r.kind == codelens_core.ReferenceKind.Inheritance]
        assert len(inherit_refs) == 0

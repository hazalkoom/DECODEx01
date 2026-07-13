"""
tests/parser/test_return_types.py
Phase 1A: Verify real return type extraction from Python type annotations
and C++ function return types (replacing the old hardcoded "auto" fallback).
"""
import textwrap
import codelens_core


class TestPythonReturnTypes:
    """Python `-> Type` annotation extraction via Tree-sitter `return_type` field."""

    def _parse(self, source: str):
        p = codelens_core.ASTParser()
        p.set_language("python")
        return p.analyze_file("dummy.py", source)

    def test_simple_type_annotation(self):
        """def foo() -> int  should yield return_type == 'int'."""
        ctx = self._parse("def foo() -> int:\n    return 1\n")
        syms = {s.name: s for s in ctx.symbols}
        assert "foo" in syms
        assert syms["foo"].return_type == "int"

    def test_none_return_annotation(self):
        """def bar() -> None  should yield return_type == 'None'."""
        ctx = self._parse("def bar() -> None:\n    pass\n")
        syms = {s.name: s for s in ctx.symbols}
        assert syms["bar"].return_type == "None"

    def test_generic_return_annotation(self):
        """def baz() -> list[str]  should yield return_type == 'list[str]'."""
        ctx = self._parse("def baz() -> list[str]:\n    return []\n")
        syms = {s.name: s for s in ctx.symbols}
        assert syms["baz"].return_type == "list[str]"

    def test_optional_return_annotation(self):
        """def maybe() -> Optional[int]  should yield the full Optional type."""
        src = textwrap.dedent("""\
            from typing import Optional
            def maybe() -> Optional[int]:
                return None
        """)
        ctx = self._parse(src)
        syms = {s.name: s for s in ctx.symbols}
        assert syms["maybe"].return_type == "Optional[int]"

    def test_unannotated_function_falls_back_to_auto(self):
        """Functions with no annotation should still return 'auto'."""
        ctx = self._parse("def untyped():\n    pass\n")
        syms = {s.name: s for s in ctx.symbols}
        assert syms["untyped"].return_type == "auto"

    def test_class_has_empty_return_type(self):
        """Classes should have an empty return_type string (not 'auto')."""
        ctx = self._parse("class MyClass:\n    pass\n")
        syms = {s.name: s for s in ctx.symbols}
        assert syms["MyClass"].return_type == ""

    def test_method_return_annotation_inside_class(self):
        """Methods inside a class should also extract return types correctly."""
        src = textwrap.dedent("""\
            class Server:
                def start(self) -> bool:
                    return True
                def stop(self):
                    pass
        """)
        ctx = self._parse(src)
        syms = {s.name: s for s in ctx.symbols}
        assert syms["start"].return_type == "bool"
        assert syms["stop"].return_type == "auto"


class TestCppReturnTypes:
    """C++ return type extraction from `function_definition.type` field."""

    def _parse(self, source: str):
        p = codelens_core.ASTParser()
        p.set_language("cpp")
        return p.analyze_file("dummy.cpp", source)

    def test_int_return_type(self):
        """int foo()  should yield return_type == 'int'."""
        ctx = self._parse("int foo() { return 1; }\n")
        syms = {s.name: s for s in ctx.symbols}
        assert "foo" in syms
        assert syms["foo"].return_type == "int"

    def test_bool_return_type(self):
        ctx = self._parse("bool is_valid() { return true; }\n")
        syms = {s.name: s for s in ctx.symbols}
        assert syms["is_valid"].return_type == "bool"

    def test_void_return_type(self):
        ctx = self._parse("void do_work() { }\n")
        syms = {s.name: s for s in ctx.symbols}
        assert syms["do_work"].return_type == "void"

    def test_string_return_type(self):
        ctx = self._parse('std::string get_name() { return "hello"; }\n')
        syms = {s.name: s for s in ctx.symbols}
        assert syms["get_name"].return_type == "std::string"

from typing import List, Optional
from sqlalchemy import String, Integer, Float, ForeignKey, Index
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class FileRecord(Base):
    __tablename__ = "files"

    id: Mapped[int] = mapped_column(primary_key=True)
    filepath: Mapped[str] = mapped_column(String, unique=True, index=True)
    language: Mapped[str] = mapped_column(String, index=True)
    last_modified: Mapped[float] = mapped_column(Float, default=0.0)
    # Relationships
    symbols: Mapped[List["SymbolRecord"]] = relationship(back_populates="file", cascade="all, delete-orphan")
    dependencies: Mapped[List["DependencyRecord"]] = relationship(back_populates="file", cascade="all, delete-orphan")
    references: Mapped[List["ReferenceRecord"]] = relationship(back_populates="file", cascade="all, delete-orphan")

class SymbolRecord(Base):
    __tablename__ = "symbols"

    id: Mapped[int] = mapped_column(primary_key=True)
    file_id: Mapped[int] = mapped_column(ForeignKey("files.id", ondelete="CASCADE"), index=True)
    
    name: Mapped[str] = mapped_column(String, index=True)
    fully_qualified_name: Mapped[Optional[str]] = mapped_column(String, nullable=True, index=True)
    signature: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    return_type: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    type: Mapped[str] = mapped_column(String)  # 'class' or 'function'
    docstring: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    start_line: Mapped[int] = mapped_column(Integer)
    end_line: Mapped[int] = mapped_column(Integer)

    # Relationship
    file: Mapped["FileRecord"] = relationship(back_populates="symbols")

class DependencyRecord(Base):
    __tablename__ = "dependencies"

    id: Mapped[int] = mapped_column(primary_key=True)
    file_id: Mapped[int] = mapped_column(ForeignKey("files.id", ondelete="CASCADE"), index=True)
    
    module_name: Mapped[str] = mapped_column(String, index=True)
    imported_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    line_number: Mapped[int] = mapped_column(Integer)

    # Relationship
    file: Mapped["FileRecord"] = relationship(back_populates="dependencies")

class ReferenceRecord(Base):
    __tablename__ = "references"

    id: Mapped[int] = mapped_column(primary_key=True)
    file_id: Mapped[int] = mapped_column(ForeignKey("files.id", ondelete="CASCADE"), index=True)
    
    caller_fqn: Mapped[str] = mapped_column(String, index=True)
    callee_fqn: Mapped[str] = mapped_column(String, index=True)
    kind: Mapped[str] = mapped_column(String)  # 'Call' or 'Instantiation'
    line_number: Mapped[int] = mapped_column(Integer)

    # Relationship
    file: Mapped["FileRecord"] = relationship(back_populates="references")

# Create composite indexes for faster cross-referencing lookups during AI context building
Index('idx_symbol_file_name', SymbolRecord.file_id, SymbolRecord.name)
Index('idx_dep_module', DependencyRecord.module_name)
Index('idx_ref_caller_callee', ReferenceRecord.caller_fqn, ReferenceRecord.callee_fqn)
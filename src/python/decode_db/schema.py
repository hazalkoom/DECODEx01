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

class SymbolRecord(Base):
    __tablename__ = "symbols"

    id: Mapped[int] = mapped_column(primary_key=True)
    file_id: Mapped[int] = mapped_column(ForeignKey("files.id"), index=True)
    
    name: Mapped[str] = mapped_column(String, index=True)
    type: Mapped[str] = mapped_column(String)  # 'class' or 'function'
    start_line: Mapped[int] = mapped_column(Integer)
    end_line: Mapped[int] = mapped_column(Integer)

    # Relationship
    file: Mapped["FileRecord"] = relationship(back_populates="symbols")

class DependencyRecord(Base):
    __tablename__ = "dependencies"

    id: Mapped[int] = mapped_column(primary_key=True)
    file_id: Mapped[int] = mapped_column(ForeignKey("files.id"), index=True)
    
    module_name: Mapped[str] = mapped_column(String, index=True)
    imported_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    line_number: Mapped[int] = mapped_column(Integer)

    # Relationship
    file: Mapped["FileRecord"] = relationship(back_populates="dependencies")

# Create composite indexes for faster cross-referencing lookups during AI context building
Index('idx_symbol_file_name', SymbolRecord.file_id, SymbolRecord.name)
Index('idx_dep_module', DependencyRecord.module_name)
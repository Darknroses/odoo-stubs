from re import Pattern
from typing import Any, Iterable

from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import ArrayObject as ArrayObject
from PyPDF2.generic import IndirectObject
from PyPDF2.utils import b_ as b_

DEFAULT_PDF_DATETIME_FORMAT: str
REGEX_SUBTYPE_UNFORMATED: Pattern
REGEX_SUBTYPE_FORMATED: Pattern

def _unwrapping_get(self, key, default: Any | None = ...): ...

class BrandedFileWriter(PdfFileWriter):
    def __init__(self) -> None: ...

PdfFileWriter = BrandedFileWriter

def merge_pdf(pdf_data: Iterable[bytes]) -> bytes: ...
def rotate_pdf(pdf: bytes) -> bytes: ...

class OdooPdfFileReader(PdfFileReader):
    def getAttachments(self) -> Iterable[tuple[Any, Any]]: ...

class OdooPdfFileWriter(PdfFileWriter):
    _reader: PdfFileReader | None
    is_pdfa: bool
    _header: bytes
    _ID: Any
    def __init__(self, *args, **kwargs):
        None
    def addAttachment(self, fname: str, fdata, subtype: str | None = ...) -> None: ...
    def embed_odoo_attachment(
        self, attachment: "odoo.model.ir_attachment", subtype: str | None = ...
    ) -> None: ...
    def cloneReaderDocumentRoot(self, reader: PdfFileReader) -> None: ...
    def convert_to_pdfa(self) -> None: ...
    def add_file_metadata(self, metadata_content: bytes) -> None: ...
    def _create_attachment_object(
        self, attachment: dict[str, Any]
    ) -> IndirectObject: ...

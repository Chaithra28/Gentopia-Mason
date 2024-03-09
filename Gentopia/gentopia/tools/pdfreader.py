from gentopia.tools.basetool import *
from PyPDF2 import PdfReader as PyPdfReader
from typing import AnyStr
import requests
from io import BytesIO
from pydantic import BaseModel, Field

class PDFReaderToolArgs(BaseModel):
    path: str = Field(..., description="path to the pdf file or URL")

class PDFReaderTool(BaseTool):
    """Tool that adds the capability to read a pdf file or URL."""

    name = "pdfreader"
    description = ("A tool that reads a pdf file or URL and returns its content.")

    args_schema: Optional[Type[BaseModel]] = PDFReaderToolArgs

    def _run(self, path: AnyStr) -> str:
        if path.startswith("http://") or path.startswith("https://"):
            response = requests.get(path)
            pdf_bytes = BytesIO(response.content)
            return self._extract_text_from_pdf(pdf_bytes)
        else:
            with open(path, 'rb') as pdf_file:
                return self._extract_text_from_pdf(pdf_file)

    def _extract_text_from_pdf(self, pdf_file: AnyStr) -> str:
        text = ""
        pdf = PyPdfReader(pdf_file)
        for page in pdf.pages:
            text += page.extract_text()
        pdf_file.close()
        return text

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

if __name__ == "__main__":
    ans = PyPdfReader()._run("path_to_pdf_or_url")
    print(ans)
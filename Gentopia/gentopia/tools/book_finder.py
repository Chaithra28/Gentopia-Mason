from typing import AnyStr, List, Optional, Type
from pydantic import BaseModel, Field
from gentopia.tools.basetool import BaseTool
import requests

class Search_Book_By_AuthorArgs(BaseModel):
    title: str = Field(..., description="Author of the book")

class Search_Book_By_Author(BaseTool):
    """Tool that adds the capability to search a book by its author."""

    name = "search_book_by_author"
    description = ("A tool that searches a book by its author.")

    args_schema: Optional[Type[BaseModel]] = Search_Book_By_AuthorArgs

    def _run(self, title: AnyStr) -> str:
        response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=inauthor:{title}")
        return response.json()

    async def _arun(self, *args: any, **kwargs: any) -> any:
        raise NotImplementedError

class Search_Book_By_GenreArgs(BaseModel):
    genre: str = Field(..., description="Genre of the book")

class Search_Book_By_Genre(BaseTool):
    """Tool that adds the capability to search a book by its genre."""

    name = "search_book_by_genre"
    description = ("A tool that searches a book by its genre.")

    args_schema: Optional[Type[BaseModel]] = Search_Book_By_GenreArgs

    def _run(self, genre: AnyStr) -> str:
        response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=subject:{genre}")
        return response.json()

    async def _arun(self, *args: any, **kwargs: any) -> any:
        raise NotImplementedError
    
class Search_Book_By_TitleArgs(BaseModel):
    title: str = Field(..., description="Title of the book")

class Search_Book_By_Title(BaseTool):
    """Tool that adds the capability to search a book by its title."""

    name = "search_book_by_title"
    description = ("A tool that searches a book by its title.")

    args_schema: Optional[Type[BaseModel]] = Search_Book_By_TitleArgs

    def _run(self, title: AnyStr) -> str:
        response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={title}")
        return response.json()

    async def _arun(self, *args: any, **kwargs: any) -> any:
        raise NotImplementedError

if __name__ == "__main__":
    ans = Search_Book_By_Author()._run("author")
    print(ans)
    ans = Search_Book_By_Genre()._run("genre")
    print(ans)
    ans = Search_Book_By_Title()._run("title")
    print(ans)

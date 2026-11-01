from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "1984", "author": "George Orwell"},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen"},
    {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger"}]


class bookRequest(BaseModel):
	id:int



@app.get("/books/{id}") #path parameter
async def get_all_books(id:int):
	for book in books:
		if book.get("id") == id:	
			return {"book":book}
	raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/")#query parameter
async def get_book_by_author(author:str):
	book_list=[]
	for book in books:
		if book.get("author").casefold() == author.casefold():
			book_list.append(book)
	return {"list of book":book_list}

@app.post("/book/")#body parameter
async def get_books(request : bookRequest):
	list_book=[]
	for book in books:
		if book.get("id") == request.id :
			list_book.append(book)
	return {"list of book by id":list_book} 
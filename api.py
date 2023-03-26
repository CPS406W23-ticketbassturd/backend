from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/search/users/{query}")
def search_users(query: str):
    # query internal method and return the list of user objects that match search

    # example return
    return {"query": query,
            "result": [
                {
                    "user_id": "askldfjsdljsdf-234234-sdfsdf",
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "john.doe@gmail.com",
                },
                {
                    "user_id": "dfsafdsfsf-232-sdfsdf",
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "email": "jane.doe@gmail.com",
                },
                {
                    "user_id": "sdfsf3-234223434-sdfs",
                    "first_name": "Jimmy",
                    "last_name": "Carter",
                    "email": "jimmy.carter@gmail.com",
                },
                {
                    "user_id": "sdf3243-234-sdfssssdf",
                    "first_name": "Jonny",
                    "last_name": "Dephh",
                    "email": "jonny.dephh@gmail.com",
                }
            ]}

@app.get("/api/search/venues/{query}")
def search_venues(query: str):
    # query internal method and return the list of venue objects that match search

    # example return
    return {"query": query,
            "result": [
                {
                    "venue_id": "sdfsf-234223434-ss",
                    "name": "Venue 1",
                    "address": "123 Sesame Street",
                    "max_capacity": "2500"
                },
                {
                    "venue_id": "weteg-12323-sfsdfdsf",
                    "name": "Venue 2",
                    "address": "12345 Sesame Street",
                    "max_capacity": "30"
                },
                {
                    "venue_id": "wsdx-22421-fbxsb",
                    "name": "Venue 3",
                    "address": "@Drakes house lol",
                    "max_capacity": "23047324809230984"
                }
            ]}

@app.get("/api/search/events/{query}")
def search_events(query: str):
    # query internal method and return the list of events objects that match search

    # example return
    return {"query": query,
            "result": [
                {
                    "event_id": "kjklj-897897-werjkl",
                    "name": "greatest even eber lol",
                    "date": 1679851845,
                    "min_age": 19,
                    "venue": "weteg-12323-sfsdfdsf",
                },
                {
                    "event_id": "jkhklklj-234-dsfdfss",
                    "name": "greatest even eber lol",
                    "date": 1685136645,
                    "min_age": 0,
                    "venue": "wsdx-22421-fbxsb",
                },
                {
                    "event_id": "jkhklkl-2343-sf",
                    "name": "greatest even eber lol",
                    "date": 1685136645,
                    "min_age": 21,
                    "venue": "sdfsf-234223434-ss",
                },

            ]}


@app.get("/api/login/{email}/{password}")
def login(email: str, password: str):
    # query internal to verify login, return true/false based on internal method

    # example return
    return {"success": True}


@app.get("/api/create_account/{email}/{password}/{first_name}/{last_name}/{phone}")
def create_account(email: str, password: str, first_name: str, last_name: str, phone: int):
    # query internal method to creating account, return true/false based on internal method

    # example return
    return {"success": True}

@app.get("/api/payment/{user_id}/{event_id}/{numOfTickets}/{card_num}/{card_cvv}/{card_name}/{card_expMonth}/{card_expYear}")
def payment(user_id: str, event_id: str, numOfTickets: int, card_num: int, card_cvv: int, card_name: str, card_expMonth: int, card_expYear: int):
    # query internal payment method, return true/false based on internal method

    # example return
    return {"success": True}

@app.get("/api/tickets/{user_id}")
def order_history(user_id: int):
    # query internal method of ticket history for the user id, return the ticket list of the user

    # example return
    return {"user_id": user_id,
            "tickets": [
                {
                    "ticket_id": "cc2a97a8-7876-477b-9101-46828413f89a",
                    "event_id": "jkhklklj-234-dsfdfss",
                    "price": 234.23
                },
                {
                    "ticket_id": "234dfdsf-7876-477b-9101-fsfddsdff",
                    "event_id": "jkhklkl-2343-sf",
                    "price": 23.23
                },
                {
                    "ticket_id": "cc2a97a8-3424-ssss-9101-46828413f89a",
                    "event_id": "jkhklklj-234-dsfdfss",
                    "price": 22.23
                }
            ]}

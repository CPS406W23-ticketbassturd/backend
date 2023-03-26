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
                    "host_id": "sdfsf3-234223434-sdfs"
                },
                {
                    "event_id": "jkhklklj-234-dsfdfss",
                    "name": "greatest even eber lol",
                    "date": 1685136645,
                    "min_age": 0,
                    "venue": "wsdx-22421-fbxsb",
                    "host_id": "sdfsf3-234223434-sdfs"
                },
                {
                    "event_id": "jkhklkl-2343-sf",
                    "name": "greatest even eber lol",
                    "date": 1685136645,
                    "min_age": 21,
                    "venue": "sdfsf-234223434-ss",
                    "host_id": "sdfsf3-234223434-sdfs"
                }
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
def order_history(user_id: str):
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

@app.get("/api/update/account/{user_id}/{email}/{password}/{first_name}/{last_name}/{phone}")
def update_account(user_id: str, email: str, password: str, first_name: str, last_name: str, phone: int):
    # handle logic internally for what needs to get updated

    # update info

    # if all true return success

    # example return
    return {"success": True}


@app.get("/api/get/user/{user_id}")
def get_user(user_id: str):
    # query internal method to grab object and then return it

    # example return
    return {
        "user_id": "sdfsf3-234223434-sdfs",
        "first_name": "Jimmy",
        "last_name": "Carter",
        "email": "jimmy.carter@gmail.com",
        "password": "123password",
        "phone": 23442344
            }

@app.get("/api/get/venue/{venue_id}")
def get_user(venue_id: str):
    # query internal method to grab object and then return it

    # example return
    return {
        "venue_id": "sdfsf-234223434-ss",
        "name": "Venue 1",
        "address": "123 Sesame Street",
        "max_capacity": "2500",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    }

@app.get("/api/get/event/{event_id}")
def get_user(event_id: str):
    # query internal method to grab object and then return it

    # example return
    return {
        "event_id": "kjklj-897897-werjkl",
        "name": "greatest even eber lol",
        "date": 1679851845,
        "min_age": 19,
        "venue": "weteg-12323-sfsdfdsf",
        "description": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?,",
        "host_id": "sdfsf3-234223434-sdfs"
    }

@app.get("/api/get/ticket/{ticket_id}")
def get_user(ticket_id: str):
    # query internal method to grab object and then return it

    # example return
    return {
        "ticket_id": "cc2a97a8-3424-ssss-9101-46828413f89a",
        "event_id": "jkhklklj-234-dsfdfss",
        "price": 22.23
    }



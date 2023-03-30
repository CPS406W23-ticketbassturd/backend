

from typing import Union
from fastapi import FastAPI

from payment import Payment
from venue import Venue
from event import Event
from ticket import Ticket
from user import User

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/search/users/{query}")
def search_users(query: str):
    # query internal method and return the list of user objects that match search

    return {
        "query": query,
        "result": User.match_first_name(query)
    }

@app.get("/api/search/venues/{query}")
def search_venues(query: str):
    # query internal method and return the list of venue objects that match search

    return {
        "query": query,
        "result": Venue.match_name(query)
    }

@app.get("/api/search/events/{query}")
def search_events(query: str):
    # query internal method and return the list of events objects that match search

    return {
        "query": query,
        "result": Event.match_name(query)
    }


@app.get("/api/login/{email}/{password}")
def login(email: str, password: str):
    # query internal to verify login, return true/false based on internal method

    # example return
    return {"success": User.login(email, password)}


@app.get("/api/create_account/{email}/{password}/{first_name}/{last_name}/{phone}")
def create_account(email: str, password: str, first_name: str, last_name: str, phone: int):
    # query internal method to creating account, return true/false based on internal method

    # example return
    return {"success": User.create_account(email, password, first_name, last_name, phone)}

@app.get("/api/payment/{user_id}/{event_id}/{numOfTickets}/{card_num}/{card_cvv}/{card_name}/{card_expMonth}/{card_expYear}")
def payment(user_id: str, event_id: str, numOfTickets: int, card_num: int, card_cvv: int, card_name: str, card_expMonth: int, card_expYear: int):
    # query internal payment method, return true/false based on internal method

    return {"success": User.purchase_ticket(user_id, event_id, numOfTickets,
                                            card_num, card_cvv, card_name, card_expMonth, card_expYear)}

@app.get("/api/tickets/{user_id}")
def order_history(user_id: str):
    # query internal method of ticket history for the user id, return the ticket list of the user
    return User.get_ticket_history(user_id)

@app.get("/api/update/account/{user_id}/{email}/{password}/{first_name}/{last_name}/{phone}")
def update_account(user_id: str, email: str, password: str, first_name: str, last_name: str, phone: int):
    # handle logic internally for what needs to get updated

    # example return
    return {"success": User.update_account_info(user_id, email, password, first_name, last_name, phone)}


@app.get("/api/get/user/{user_id}")
def get_user(user_id: str):
    # query internal method to grab object and then return it
    account = User.from_id(user_id)
    if not account:
        return {"success": False}
    return {"success": True, "result": account.to_db_user().to_dict()}

@app.get("/api/get/venue/{venue_id}")
def get_user(venue_id: str):
    # query internal method to grab object and then return it

    ven = Venue.from_id(venue_id)
    if not ven:
        return {"success": False}
    return {"success": True, "result": ven.to_db_venue().to_dict()}

@app.get("/api/get/event/{event_id}")
def get_user(event_id: str):
    # query internal method to grab object and then return it

    eve = Event.from_id(event_id)
    if not eve:
        return {"success": False}
    return {"success": True, "result": eve.to_db_event().to_dict()}

@app.get("/api/get/ticket/{ticket_id}")
def get_user(ticket_id: str):
    # query internal method to grab object and then return it

    tick = Ticket.from_id(ticket_id)
    if not tick:
        return {"success": False}
    return {"success": True, "result": tick.to_db_ticket().to_dict()}


@app.get("/api/create_event/{name}/{description}/{date}/{venue_id}/{min_age}/{price}")
def create_event(name: str, description: str, date: str, venue_id: str, min_age: int, price: int):
    # activate internal method for creating event

    # example return
    return {
        "success": True,
        "event_id": "fifljksdjf-234234-ssdf"
    }
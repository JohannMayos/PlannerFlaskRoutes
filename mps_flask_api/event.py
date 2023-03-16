from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

EVENT = {
    "1000":{
        "event_title":"Show da Odium",
        "event_id": "1000",
        "event_description": "Show da melhor banda de manaus",
        "event_date": "22/03/2023",
        "user_id": "1000",
        "timestamp": get_timestamp()
    },
    "2000":{
        "event_title":"Shoegaze dos crias",
        "event_id": "2000",
        "event_description": "Show das melhores bandas de shoegaze",
        "event_date": "25/03/2023",
        "user_id": "2000",
        "timestamp": get_timestamp()
    },
    "3000":{
        "event_title":"Rodízio no faraó",
        "event_id": "3000",
        "event_description": "Rodizio nham nham",
        "event_date": "22/03/2023",
        "user_id": "3000",
        "timestamp": get_timestamp()
    }
}

def read_all():
    return list(EVENT.values())


def create(event):
    event_id = event.get("event_id")
    event_title = event.get("event_title", "")
    event_description = event.get("event_description", "")
    event_date = event.get("event_date", "")
    user_id = event.get("user_id")

    if event_id and event_id not in EVENT:
        EVENT[event_id] = {
            "event_id": event_id,
            "event_title": event_title,
            "event_description": event_description,
            "event_date": event_date,
            "user_id" : user_id,
            "timestamp": get_timestamp(),
        }
        return EVENT[event_id], 201
    else:
        abort(
            406,
            f"User with last name {event_id} already exists",
        )

def read_one(event_id):
    if event_id in EVENT:
        return EVENT[event_id]
    else:
        abort(
            404, f"Event ID {event_id} not found"
        )

def update(event_id, event):
    if event_id in EVENT:
        EVENT[event_id]["event_title"] = event.get("event_title", EVENT[event_id]["event_title"])
        EVENT[event_id]["event_description"] = event.get("event_description", EVENT[event_id]["event_description"])
        EVENT[event_id]["event_date"] = event.get("event_date", EVENT[event_id]["event_date"])
        EVENT[event_id]["timestamp"] = get_timestamp()
        return EVENT[event_id]
    else:
        abort(
            404,
            f"Event ID {event_id} not found"
        )

def delete(event_id):
    if event_id in EVENT:
        del EVENT[event_id]
        return make_response(
            f"{event_id} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Event ID {event_id} not found"
        )
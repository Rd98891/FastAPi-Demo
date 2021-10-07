"""
Demonstration of basic FastAPI BackgroundTasks usage in Python @RD_2021
"""

from fastapi import FastAPI, BackgroundTasks
from time import sleep


app = FastAPI()


def send_email(message):
    sleep(5)
    print(f"Sending Email {message}")


@app.get('/')
async def index(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, ".......Hello There!")
    return {"result": "success"}
# This executes after the results have been shown and the user doesn't have to wait.

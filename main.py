import requests
from datetime import datetime, date
from tkinter import *
from tkcalendar import *

USER = "cecesciuto"
TOKEN = "bjkdw7482bjf"
GRAPH_ID = "graph1"


def update_reading_graph():
    update_graph1_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}"
    today = date.selection_get().strftime("%Y%m%d")
    quantity = str(pages.get())
    graph1_config = {
        "date": today,
        "quantity": quantity,
    }
    update_response = requests.post(url=update_graph1_endpoint, json=graph1_config, headers=headers)
    print(update_response.text)
    window.destroy()



# # created User
pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": "bjkdw7482bjf",
    "username": "cecesciuto",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

# creating a graph
graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Reading",
    "unit": "pages",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

year = date.today().year
month = date.today().month
day = date.today().day
window = Tk()
window.title("Reading Log")
window.config(padx=20, pady=20)
pages = Entry(width=7)
pages.grid(column=1, row=0)
pages_label = Label(text="Pages Read", font="Arial 14")
pages_label.grid(column=2, row=0)
date = Calendar(window, font="Arial 14",selectmode='day', year=year, month=month, day=day)
date.grid(column=1, row=1, columnspan=2)
submit = Button(text="Submit", command=update_reading_graph)
submit.grid(column=1, row=2, columnspan=2)
window.mainloop()


import requests


url = "http://localhost:3010/api/books"
auth = requests.auth.HTTPBasicAuth("admin", "password")


def list_books():
    books = requests.get(url).json()

    for book in books:
        print("{:3d} {}".format(book["id"], book["name"]))

def add_books():
    books = [
        ("ごんぎつね", "新美南吉"),
        ("山月記", "中島敦")
    ]

    for book in books:
        data = {"name": book[0], "author": book[1]}
        requests.post(url, json=data, auth=auth)


if __name__ == "__main__":
    list_books()
    # add_books()

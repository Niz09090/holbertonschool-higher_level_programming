#!/usr/bin/python3
"""Module for fetching and processing posts from JSONPlaceholder"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches all posts and prints their titles"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        for post in response.json():
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetches all posts and saves them to a CSV file"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = [{"id": p["id"], "title": p["title"], "body": p["body"]}
                 for p in response.json()]
        with open("posts.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)

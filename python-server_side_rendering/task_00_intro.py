#!/usr/bin/python3
"""Module for generating personalized invitation files from a template"""


def generate_invitations(template, attendees):
    """Generate invitation files from template and attendees list"""
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, 1):
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            content = content.replace("{" + key + "}", str(value) if value is not None else "N/A")
        with open("output_{}.txt".format(i), "w") as f:
            f.write(content)

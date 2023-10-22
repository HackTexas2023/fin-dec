import requests
from bs4 import BeautifulSoup

# Replace this URL with the actual URL of the form
url = "https://form.jotform.com/232942572878167"

# Send an HTTP GET request to the form URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the form element
    form = soup.find("form", {"id": "232942572878167"})

    # Initialize a dictionary to store the form data
    form_data = {}

    # Loop through form fields and extract data
    for input_element in form.find_all("input"):
        field_name = input_element.get("name")
        field_value = input_element.get("value")
        if field_name:
            form_data[field_name] = field_value

    # You can also handle other types of form fields (e.g., textareas, checkboxes, etc.) in a similar way

    # Print or use the form data as needed
    print(form_data)
else:
    print("Failed to retrieve the form.")
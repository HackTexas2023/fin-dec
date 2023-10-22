import requests
from bs4 import BeautifulSoup

# URL of the Jotform survey
url = "https://form.jotform.com/232942572878167"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the form fields by finding the input elements
    form_fields = soup.find_all('input')
    
    # Extract data from the form fields
    data = {}
    for field in form_fields:
        # Get the input field's name and value
        field_name = field.get('name')
        field_value = field.get('value', '')
        
        # Store the data in a dictionary
        data[field_name] = field_value
    
    # Print the extracted data
    for key, value in data.items():
        print(f"{key}: {value}")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

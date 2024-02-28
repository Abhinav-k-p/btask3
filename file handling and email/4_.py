# Create a program that attempts to connect to a website and prints the HTML content if successful. Use a try-except-else block to handle the requests.exceptions.RequestException exception and display an error message if the connection fails.


import requests

try:
    # give a url
    url = "https://www.w3schools.com/w3css/w3css_templates.asp#gsc.tab=0"  
    response = requests.get(url)
    response.raise_for_status()

    # Successful connection, print the HTML content
    print(response.text)
    
except requests.exceptions.RequestException as e:
    print(f"Error: Connection failed. {e}") 
else:
    print("Website accessed successfully!")  

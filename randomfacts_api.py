import requests

url = "https://uselessfacts.jsph.pl/random.json?language=en"

def get_random_fact():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"Did you know? {fact_data['text']}")
    else:
        print("Failed to fetch fact. Please try again later.")

while True:
    user_input = input("Press Enter to get a random fact or type 'exit' to quit.")               
    if user_input.lower() == 'exit':
        print("Goodbye!")
        
    get_random_fact()
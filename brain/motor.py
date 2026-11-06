import requests

response= requests.get("https://www.googleapis.com/books/v1/volumes?q=hunger+games&key=AIzaSyDj6ScWLVH1OHFhQdAgENYVn5WEoDOh6CM")
response.text
print(response.status_code)
if response.status_code == 200:
    print("Request is sent successfully")

question=input("what book are you looking for?")
question=question.replace(" ","+")
response=requests.get("https://www.googleapis.com/books/v1/volumes?q="+question+"&key=AIzaSyDj6ScWLVH1OHFhQdAgENYVn5WEoDOh6CM")
info_data=response.json()

print("your book is found here are the details:", 
        info_data['items'][0]['volumeInfo'])
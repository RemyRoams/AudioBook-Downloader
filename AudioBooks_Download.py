import requests
from bs4 import BeautifulSoup

# Change - the url
# Change - the file_name variable

url = 'website url'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

aud_books = soup.find_all('source', {'type': 'audio/mpeg'})
print(aud_books)

count = 0

for aud in aud_books:
    book = aud.get("src")
    print(book)
    count += 1

#from ChatGPT
    file_name = f"Book_Name_{count}.mp3"

    # Send a GET request to download the file
    response = requests.get(book, stream=True)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        with open(file_name, "wb") as file:
            for chunk in response.iter_content(1024):  # Download in chunks of 1024 bytes
                file.write(chunk)
        print(f"Download complete: {file_name}")
    else:
        print("Failed to download the file. Check the URL or try again later.")

print("done")
import urllib.parse
import requests
import os

directory_name = "Fetched_Images"

url = input("Enter the image URL: ")

os.makedirs(directory_name, exist_ok=True)

try:
    # 1. We try to get the response.
    response = requests.get(url)

    # 2. We check if the request was successful.
    # If not, this line will raise an HTTPError.
    response.raise_for_status()

    # 3. Parse the URL to extract the filename
    parsed_url = urllib.parse.urlparse(url)
    image_filename = os.path.basename(parsed_url.path)
    print("Image fetched successfully!")

    # 4. Check if the filename is empty and set a default
    if not image_filename:
        image_filename = "downloaded_image.jpg"
        print(f"No filename found in URL. Saving as: {image_filename}")

    # 5. Create the full file path
    file_path = os.path.join(directory_name, image_filename)

    # 6. Save the image to the file
    with open(file_path, 'wb') as f:
        f.write(response.content)
    
    print(f"Image saved successfully to {file_path}")

except requests.exceptions.HTTPError as e:
    # 7. If an HTTPError was raised, the code jumps here.
    print(f"HTTP error occurred: {e}")
except requests.exceptions.ConnectionError as e:
    # 8. This is good practice to also catch if there's no internet connection, or a bad URL format
    print(f"Connection error occurred: {e}")
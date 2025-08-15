import requests

def download_video(url, local_filename):
    # Send a GET request to the URL
    response = requests.get(url, stream=True)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Open a file in binary write mode
        with open(local_filename, 'wb') as file:
            # Write the content of the response to the file
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Video downloaded and saved as {local_filename}")
    else:
        print(f"Failed to download video. Status code: {response.status_code}")

# URL of the video
video_url = 'https://file-examples.com/storage/fe44eeb9cb66ab8ce934f14/2020/03/file_example_WEBM_1920_3_7MB.webm'

# Local filename to save the video
local_filename = 'downloaded_video.webm'

# Call the function to download the video
download_video(video_url, local_filename)
import requests

# Example API endpoint that provides image URL
api_url = "https://9bpn4rbmt4.execute-api.us-east-1.amazonaws.com/qa/recognize?project_id=82"

try:
    response = requests.get(api_url)
    if response.status_code == 200:
        image_url = response.json()["https://qa-gvc-bucket.s3.amazonaws.com/collection/22306?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQUNULULY25RL7LGX%2F20240627%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240627T170948Z&X-Amz-Expires=600&X-Amz-SignedHeaders=host&X-Amz-Signature=f7f53365ae18baada90d13970d3b657ed1b376004f77811ff78f52710c2d9c80"]
        print("Image URL:", image_url)
    else:
        print(f"Failed to fetch image URL. Status code: {response.status_code}")

except requests.RequestException as e:
    print(f"Error fetching image URL: {e}")

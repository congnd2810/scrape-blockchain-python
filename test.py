import base64
import requests

# OpenAI API Key
api_key = ""

# Function to encode the image


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# Path to your image
image_path1 = "./tonkin-1-600-piastres-1905.jpg"
image_path2 = './tonkin-1-600-piastres-1905 (1).jpg'
# Getting the base64 string
base64_image1 = encode_image(image_path1)
base64_image2 = encode_image(image_path2)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "đây là 2 mặt đồng xu của nước nào? thông tin chi tiết của đồng tiền này"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image2}"
                    }
                }
            ]
        }
    ],
    "max_tokens": 2000
}

response = requests.post(
    "https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())

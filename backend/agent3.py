from flask import Flask, jsonify
from flask_cors import CORS  # Enable CORS for React Native
from google import genai
import os
from dotenv import load_dotenv
import PIL.Image

def ask_gemini():

    load_dotenv()
    api_key = os.getenv("API_KEY")

    client = genai.Client(api_key=api_key)

    prompt = """ You are an expert in fashion and sneaker identification. Analyze the provided image of a shoe and return the following details:
      Brand/Make (e.g., Nike, Adidas, New Balance)
      Model Name (e.g., Air Jordan 1, Yeezy Boost 350)
      Colorway or Edition (e.g., Bred, Triple White, Off-White x Nike)
      Style or Category (e.g., running shoe, basketball sneaker, casual, skateboarding)
      Distinguishing Features (e.g., materials, logos, design patterns, lacing system)
      Estimated Release Year or Collection (if identifiable)
      Be as specific and detailed as possible. If unsure, provide the closest match or a list of possible models."""

    image = PIL.Image.open('sneaker.png')

    response = client.models.generate_content(
      model="gemini-2.0-flash",
      contents=[image, prompt])

    return response.text

app = Flask(__name__)
CORS(app)  # Allow requests from React Native

@app.route('/agent3', methods=['GET'])
def home():
    response = ask_gemini()
    return jsonify({"message": response})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify, render_template
import openai
from pydantic import BaseModel, ValidationError, validator
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# Define Pydantic models for request and response
class PromptSchema(BaseModel):
    prompt: str

    @validator('prompt')
    def validate_prompt(cls, v):
        if len(v.strip()) < 5:
            raise ValueError("Prompt is too short. Please provide more details.")
        forbidden_words = ["forbidden", "banned"]
        if any(word in v.lower() for word in forbidden_words):
            raise ValueError("The prompt contains forbidden content.")
        return v

class ResponseSchema(BaseModel):
    completion: str

# Function to generate response using OpenAI API
def generate_response(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Update to a supported model
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,  # Adjust as needed
            temperature=0.7  # Adjust creativity level as needed
        )
        return response.choices[0].message['content'].strip()
    except openai.error.RateLimitError:
        # Handle quota exceeded error
        raise RuntimeError("You have exceeded your OpenAI API quota. Please check your billing details.")
    except Exception as e:
        raise RuntimeError(f"OpenAI API error: {e}")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.get_json()
    try:
        # Validate input data using Pydantic
        prompt_obj = PromptSchema(**data)
        # Generate response from OpenAI
        response_text = generate_response(prompt_obj.prompt)
        # Create response object
        response_obj = ResponseSchema(completion=response_text)
        return jsonify(response_obj.dict())
    except ValidationError as ve:
        # Return validation errors
        return jsonify({"error": ve.errors()}), 400
    except RuntimeError as re:
        # Return quota exceeded or other runtime errors
        return jsonify({"error": str(re)}), 429  # 429 Too Many Requests
    except Exception as e:
        # Return any other errors
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

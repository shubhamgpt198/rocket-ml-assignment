from flask import Flask, request, jsonify
import openai
import json

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = "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"

@app.route('/sentiment', methods=['POST'])
def sentiment_analysis():
    """Endpoint for sentiment analysis API.
    
    Accepts a JSON request containing a 'text' field with the input text to be analyzed.
    Uses the GPT-3 model to perform sentiment analysis and detect topic and language of the input text.
    Returns a JSON response containing the sentiment, topic, and language as lowercase strings.
    """
    # Get the input text from the request
    input_text = request.json['text']

    # Use GPT-J to do sentiment analysis
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Sentiment analysis of the following text and detect topic and language.:\n\n{input_text}.",
            max_tokens=256,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Extract the sentiment from the OpenAI response
        print(response)
        sentiment = response.choices[0].text.strip()

        # Extract the values from the response
        response = sentiment.split('\n')
        sentiment = response[0].split(":")[-1].strip()
        topic = response[1].split(":")[-1].strip()
        language = response[2].split(":")[-1].strip()

        # Convert the values to a dictionary
        data = {
            "sentiment": sentiment.lower(),
            "topic": topic.lower(),
            "language": language.lower()
        }

        # Return the sentiment as a JSON response
        return jsonify({'response_data': data}), 200
    except:
        return jsonify({'response_data': "Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)

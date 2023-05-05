from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = "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"

# Define the endpoint for the sentiment analysis API
@app.route('/sentiment', methods=['POST'])
def sentiment_analysis():
    # Get the input text from the request
    input_text = request.json['text']
    
    # Use GPT-J to do sentiment analysis
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Sentiment analysis of the following text and detect topic and language:\n\n{input_text}",
        max_tokens=256,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    # Extract the sentiment from the OpenAI response
    print(response)
    sentiment = response.choices[0].text.strip()
    
    # Return the sentiment as a JSON response
    return jsonify({'response_data': sentiment})

if __name__ == '__main__':
    app.run(debug=True)

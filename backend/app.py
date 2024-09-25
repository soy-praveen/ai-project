from flask import Flask, request, jsonify
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

app = Flask(__name__)

model_name = "bert-base-uncased"
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
tokenizer = AutoTokenizer.from_pretrained(model_name)

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text')
    aspect = data.get('aspect')
    
    combined_text = f"{aspect}: {text}"
    inputs = tokenizer(combined_text, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=-1).tolist()[0]
    
    sentiment = "Positive Tone" if probabilities[1] > probabilities[0] else "Negative Tone"
    
    return jsonify({"result": sentiment})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask

app = Flask(__name__)

# A simulated list of existing models (update this based on your lab's setup)
existing_models = ["Beedle", "Crossroads", "model_s", "mustang", "civic", "corolla"]

# Task 3: Set up '/' route
@app.route('/')
def home():
    return "Welcome to Flatiron Cars"

# Task 3: Set up '/models/<model>' route
@app.route('/<model>')
def check_model(model):
    # Check if the model exists in the array
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
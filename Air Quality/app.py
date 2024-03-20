from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple function for air quality prediction
def predict_air_quality(temperature, humidity, pressure):
    # Your prediction logic here (replace with your actual model)
    # This is just a placeholder
    prediction = "Good" if temperature < 20 and humidity < 40 and pressure > 60 else "Poor"
    return prediction

    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        pressure = float(request.form['pressure'])

        prediction = predict_air_quality(temperature, humidity, pressure)

        return jsonify({'result': prediction})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

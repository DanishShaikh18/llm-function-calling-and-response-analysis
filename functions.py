def calculate(a, b, operation):
    if operation == "add":
        return a + b

    if operation == "multiply":
        return a * b

    return "Unsupported operation"


def get_weather(city):
    weather_data = {
        "Mumbai": "31°C, Cloudy",
        "Delhi": "36°C, Sunny",
        "Bangalore": "27°C, Rainy"
    }

    return weather_data.get(city, "Weather unavailable")
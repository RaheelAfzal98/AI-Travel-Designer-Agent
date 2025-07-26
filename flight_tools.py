def get_mock_flights(destination, budget):
    city = destination.split(",")[0].strip()
    flights_db = {
        "Patagonia": ["Economy: $1200 (18hrs)", "Business: $2500 (18hrs)"],
        "Queenstown": ["Economy: $1500 (20hrs)", "Premium: $2200 (20hrs)"],
        "Bali": ["Economy: $850 (15hrs)", "Business: $1500 (15hrs)"],
        "Paris": ["Economy: $600 (7hrs)", "Premium: $900 (7hrs)"],
        "New York": ["Economy: $400 (6hrs)", "First: $1200 (6hrs)"],
        "Tokyo": ["Economy: $900 (11hrs)", "Premium: $1400 (11hrs)"],
        "Rome": ["Economy: $700 (8hrs)", "Business: $1300 (8hrs)"]
    }
    return flights_db.get(city, [
        f"Economy: ${800+(len(city)%500)} (10hrs)", 
        f"Business: ${1500+(len(city)%500)} (10hrs)"
    ])
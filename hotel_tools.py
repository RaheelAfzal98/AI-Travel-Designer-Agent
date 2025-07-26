def get_mock_hotels(destination, budget):
    city = destination.split(",")[0].strip()
    hotels_db = {
        "Patagonia": ["Eco Lodge ($200/night)", "Mountain Resort ($350/night)"],
        "Queenstown": ["Adventure Hotel ($180/night)", "Lakeview Resort ($300/night)"],
        "Bali": ["Beach Resort ($200/night)", "Villa ($150/night)", "Hostel ($30/night)"],
        "Paris": ["Luxury Hotel ($300/night)", "Boutique ($180/night)", "Apartment ($100/night)"],
        "New York": ["5-Star Hotel ($400/night)", "Mid-Range ($250/night)", "Budget ($120/night)"],
        "Tokyo": ["Ryokan ($250/night)", "Business Hotel ($180/night)", "Capsule ($50/night)"],
        "Rome": ["Historic Hotel ($280/night)", "B&B ($150/night)", "Hostel ($40/night)"]
    }
    return hotels_db.get(city, [
        "Luxury Resort ($300/night)",
        "Boutique Hotel ($150/night)",
        "Budget Hostel ($50/night)"
    ])
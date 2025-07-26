from .base_agent import BaseAgent
from tools.flight_tools import get_mock_flights
from tools.hotel_tools import get_mock_hotels

class BookingAgent(BaseAgent):
    def get_flights(self, destination, budget):
        try:
            return get_mock_flights(destination, budget)
        except Exception as e:
            print(f"\n⚠️ Using default flight data (Error: {str(e)})")
            base_price = 300 + (len(destination) * 10)
            return [
                f"Economy: ${base_price} (10hrs)",
                f"Premium: ${base_price*1.5} (10hrs)",
                f"Business: ${base_price*2} (10hrs)"
            ]

    def suggest_hotels(self, destination, budget):
        try:
            return get_mock_hotels(destination, budget)
        except Exception as e:
            print(f"\n⚠️ Using default hotel data (Error: {str(e)})")
            return [
                "Luxury Resort ($300/night)",
                "Boutique Hotel ($150/night)",
                "Budget Hostel ($50/night)"
            ]
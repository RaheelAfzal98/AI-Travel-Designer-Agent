from .base_agent import BaseAgent

class DestinationAgent(BaseAgent):
    def suggest_destinations(self, travel_style):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{
                    "role": "system",
                    "content": "Suggest 5 specific travel destinations matching: " + travel_style + ". Return one destination per line."
                }],
                temperature=0.7,
                extra_headers=self.headers
            )
            destinations = [x.strip() for x in response.choices[0].message.content.split("\n") if x.strip()]
            return destinations[:5]
        except Exception as e:
            print(f"\n⚠️ Using default destinations (API error: {str(e)})")
            return self.get_default_destinations(travel_style)

    def get_default_destinations(self, style):
        style = style.lower()
        if "adventur" in style:
            return ["Patagonia, Argentina", "Queenstown, New Zealand", "Kathmandu, Nepal", "Anchorage, Alaska", "San José, Costa Rica"]
        elif "relax" in style:
            return ["Bali, Indonesia", "Malé, Maldives", "Santorini, Greece", "Maui, Hawaii", "Phuket, Thailand"]
        elif "cult" in style:
            return ["Kyoto, Japan", "Rome, Italy", "Cairo, Egypt", "Paris, France", "Istanbul, Turkey"]
        return ["Bali, Indonesia", "Paris, France", "New York City, USA", "Tokyo, Japan", "Rome, Italy"]
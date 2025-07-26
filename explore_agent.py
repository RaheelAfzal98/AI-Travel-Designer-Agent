from .base_agent import BaseAgent

class ExploreAgent(BaseAgent):
    def create_itinerary(self, destination, days):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{
                    "role": "system",
                    "content": f"Create a detailed {days}-day itinerary for {destination} with daily activities and food suggestions."
                }],
                temperature=0.7,
                extra_headers=self.headers
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"\n⚠️ Using default itinerary (API error: {str(e)})")
            return self.get_default_itinerary(destination, days)

    def get_default_itinerary(self, dest, days):
        return f"""Default {days}-Day Itinerary for {dest}:
        
Day 1: Arrival & City Tour
- Morning: Explore downtown area
- Lunch: Local cuisine at recommended restaurant
- Afternoon: Visit main landmarks
- Dinner: Traditional dishes at popular local spot

Day 2: Cultural Experience
- Morning: Museum visit
- Lunch: Cafe near cultural sites
- Afternoon: Guided historical tour
- Dinner: Themed restaurant

Day 3: Nature Exploration
- Morning: Park or natural attraction
- Lunch: Picnic or nearby cafe
- Afternoon: Outdoor activities
- Dinner: Relaxing meal with views

Day 4: Free Day
- Explore at your own pace
- Shopping or optional activities

Day 5: Departure
- Breakfast at hotel
- Final sightseeing before departure"""
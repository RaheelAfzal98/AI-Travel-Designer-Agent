from dotenv import load_dotenv
from agents.destination_agent import DestinationAgent
from agents.booking_agent import BookingAgent
from agents.explore_agent import ExploreAgent

def display_menu(options, title):
    print(f"\n{title}:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(options):
                return choice - 1
            print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")

def main():
    load_dotenv()
    print("\n✈️ AI Travel Designer")
    print("Plan your perfect trip with AI assistance\n")
    
    destination_agent = DestinationAgent()
    booking_agent = BookingAgent()
    explore_agent = ExploreAgent()

    # Get travel preferences
    travel_style = input("How would you describe your travel style? (e.g., adventurous, relaxing, cultural): ")
    budget = input("What's your budget range? (e.g., $1000-$2000): ")
    duration = input("How many days is your trip? ")

    # Get destinations
    destinations = destination_agent.suggest_destinations(travel_style)
    dest_idx = display_menu(destinations, "Suggested Destinations")
    selected_dest = destinations[dest_idx]

    # Get flights
    print("\n✈️ Available Flights:")
    flights = booking_agent.get_flights(selected_dest, budget)
    for flight in flights:
        print(f"- {flight}")

    # Get hotels
    print("\n🏨 Recommended Hotels:")
    hotels = booking_agent.suggest_hotels(selected_dest, budget)
    for hotel in hotels:
        print(f"- {hotel}")

    # Get itinerary
    print("\n📅 Suggested Itinerary:")
    itinerary = explore_agent.create_itinerary(selected_dest, duration)
    print(itinerary)

if __name__ == "__main__":
    main()
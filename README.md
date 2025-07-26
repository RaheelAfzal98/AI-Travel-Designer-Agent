# AI Travel Designer Agent 🌍✈️🏨

An intelligent travel planning system that coordinates between specialized agents to create personalized travel experiences.

## Features ✨

- **Mood-based Destination Suggestions** - Recommends places based on your mood (adventurous, relaxing, etc.)
- **Interest Matching** - Tailors suggestions to your specific interests
- **Multi-Agent Coordination**:
  - 🗺️ DestinationAgent - Finds perfect locations
  - ✈️ BookingAgent - Handles flights and hotels
  - 🍽️ ExploreAgent - Suggests attractions and restaurants
- **Mock API Integration** - Simulates real travel booking systems

## Installation 🛠️

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/AI-Travel-Designer.git
   cd AI-Travel-Designer
   ```

2. **Set up virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   - Create `.env` file

## Project Structure 📂

```
AI_Travel_Designer/
├── agents/
│   ├── destination_agent.py   # Handles destination recommendations
│   ├── booking_agent.py       # Manages flights and hotels
│   └── explore_agent.py       # Suggests activities and dining
├── tools/
│   ├── flight_tools.py        # Flight booking utilities
│   └── hotel_tools.py         # Hotel booking utilities
├── main.py                    # Main orchestrator
├── requirements.txt           # Dependencies
└── .env                       # Environment configuration
```

## Usage 🚀

1. **Run the system**:
   ```bash
   python main.py
   ```

2. **Sample workflow**:
   ```python
   # Initialize agents
   travel_designer = TravelDesigner()
   
   # Plan a trip
   trip = travel_designer.plan_trip(
       mood="adventurous",
       interests=["hiking", "local culture"],
       budget="medium",
       travel_dates={"departure": "2023-12-15", "return": "2023-12-22"}
   )
   ```

## Agent Details 🤖

### 1. DestinationAgent
- **Input**: Mood, interests list
- **Output**: JSON with recommended destinations
- **Methods**:
  - `suggest_destinations(mood, interests)`

### 2. BookingAgent
- **Input**: Location, dates, budget
- **Output**: Flight/hotel options
- **Methods**:
  - `get_flights(origin, destination, date)`
  - `suggest_hotels(destination, check_in, check_out, budget)`

### 3. ExploreAgent
- **Input**: Destination, preferences
- **Output**: Activities and dining suggestions
- **Methods**:
  - `suggest_attractions(destination, interests)`
  - `suggest_restaurants(destination, cuisine_preferences)`

## Dependencies 📦

- Python 3.8+
- OpenAI Python SDK
- python-dotenv
- Requests

## Future Enhancements 🔮

- [ ] Real API integrations (Skyscanner, Booking.com)
- [ ] Web interface with FastAPI
- [ ] User account system
- [ ] Trip budget calculator
- [ ] Weather integration

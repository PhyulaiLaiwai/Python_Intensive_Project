import csv

def read_data(filename):
    """ 
    Read a CSV file and collect temperatures for each city.
    Returns a dictionary where each city maps to a list of temperatures.     
    """
    weather_data = {}
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)           # Dictionary format reader
            for row in reader:
                city = row["City"].strip()          # Clean up any accidental hidden spaces
                
                try:
                    temps = float(row["Temperature"])
                except ValueError:
                    # FIXED: Internal double quotes changed to single quotes
                    print(f" Warning⚠️ Invalid temperature '{row['Temperature']}' for {city}. Skipping.")
                    continue                        # FIXED: Skips adding to dictionary if conversion fails
                
                if city not in weather_data:
                    weather_data[city] = []
                weather_data[city].append(temps)
                
    except FileNotFoundError:
        print("❌ File not found! Please check the file path again.")
        
    return weather_data

def show_weather_summary(weather_data):
    """
    Print average, max, and min temperature for each city.
    """
    if not weather_data:
        print("No weather data to display ❌")
        return
        
    print("\n" + "="*35)
    print("🌍 WEATHER SUMMARY REPORT")
    print("="*35)
    
    for city, temps in weather_data.items(): 
        avg_temp = sum(temps) / len(temps)
        max_temp = max(temps)
        min_temp = min(temps)

        # Beautifully formatted to match your requested box aesthetic!
        print(f"║ {city}:")
        print(f"║   Average temperature: {avg_temp:.1f}°C")
        print(f"║   Highest temperature: {max_temp:.1f}°C")
        print(f"║   Lowest temperature:  {min_temp:.1f}°C")
       

def main():
    print("WEATHER ANALYZER 🌡️ ⛅")
    filename = 'project_4_resources\starter\weather.csv' 
    data = read_data(filename)
    show_weather_summary(data)

if __name__ == "__main__":
    main()
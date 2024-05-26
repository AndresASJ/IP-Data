import requests
import folium

def is_number(value):  # check if the value can become a float, else it has a char
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_google_geolocation(api_key):
    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}'
    data = {
        "considerIp": "true" #instructs the API to consider the IP address of the request when determining the location.
    }
    try:
        response = requests.post(url, json=data, timeout=5)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Google Geolocation request failed: {e}")
        return None

# Google API key
api_key = 'key'

while True:
    user_ip = input("Please enter a public IP Address: ")
    ip_parts = user_ip.split(".")

    # We divide into 4 parts because IP is divided into four parts, we use all() to check numbers are over 0
    if len(ip_parts) == 4 and all(is_number(part) for part in ip_parts):
        url = f"http://ip-api.com/json/{user_ip}"

        response = requests.get(url, timeout=5)
        data = response.json()

        if data["status"] == "success":
            # Use Google Geolocation API to get latitude and longitude
            google_data = get_google_geolocation(api_key)

            if google_data and 'location' in google_data:
                latitude = float(google_data['location']['lat'])
                longitude = float(google_data['location']['lng'])
                map_center = [latitude, longitude]

                # Labels for output
                labels = {
                    "query": "IP Address",
                    "country": "Country",
                    "regionName": "Region",
                    "city": "City",
                    "lat": "Latitude",
                    "lon": "Longitude"
                }

                for key, value in data.items():
                    if key in labels:
                        print(f"{labels[key]}: {value}")

                print(f"Latitude: {latitude}")
                print(f"Longitude: {longitude}")

                # Create and save the map
                map = folium.Map(location=map_center, zoom_start=12)
                folium.Marker(map_center, popup=user_ip).add_to(map)
                map.save("map.html")

                print("Map has been saved as map.html")
                break  # We break right here because we got the IP info
            else:
                print("Google Geolocation lookup failed.")
                if google_data:
                    print(google_data)  # Print the data for debugging
        else:
            print("IP-API lookup failed.")
            print(response.status_code)
            print(data)
    else:
        print("Please enter a valid IP address.")

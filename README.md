# IP Geolocation and Mapping Tool

This project provides a simple tool for geolocating a public IP address using the IP-API service and Google Geolocation API. It also creates a map showing the location using the Folium library and saves it as an HTML file.

## Features

- **IP Validation:** Ensures that the input provided by the user is a valid IP address.
- **IP Geolocation Lookup:** Fetches location data such as country, region, city, latitude, and longitude based on the IP address using the IP-API service.
- **Google Geolocation:** Uses the Google Geolocation API to get a more accurate latitude and longitude.
- **Map Generation:** Generates an interactive map centered on the IP address's location using the Folium library and saves it as `map.html`.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- The `requests` and `folium` Python libraries installed. You can install them using pip:

    ```bash
    pip install requests folium
    ```

- A valid Google API key with access to the Geolocation API. You can get one from the [Google Cloud Console](https://console.cloud.google.com/).

## Usage

1. Clone the repository or copy the script to your local machine.

2. Replace the `api_key` variable in the script with your Google API key:

    ```python
    api_key = 'your_google_api_key_here'
    ```

3. Run the script:

    ```bash
    python geolocation_script.py
    ```

4. When prompted, enter the public IP address you want to geolocate.

5. If the IP address is valid, the script will output the location details and generate a map showing the IP address's location. The map will be saved as `map.html` in the same directory.


## Troubleshooting

- **Google Geolocation API Request Failed:** Ensure that your Google API key is correct and has the necessary permissions.
- **IP-API Lookup Failed:** Check if the IP address is correct and ensure that the IP-API service is accessible.
- **Invalid IP Address:** Make sure the IP address entered is in the correct format (e.g., `192.168.1.1`).

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Resources

- [IP-API](http://ip-api.com/) for the IP geolocation service.
- [Google Geolocation API](https://developers.google.com/maps/documentation/geolocation/overview) for additional geolocation services.
- [Folium](https://python-visualization.github.io/folium/) for the interactive map generation.



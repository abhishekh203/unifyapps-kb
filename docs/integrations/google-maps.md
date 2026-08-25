# Google Maps connector

Source: https://www.unifyapps.com/docs/unify-integrations/google-maps
Section: integrations

---

Google Maps is a powerful mapping and location service provided by Google that allows users to access geolocation data, directions, places, and mapping services. It provides APIs to search locations, calculate distances, fetch place details, and embed maps. By integrating the Google Maps connector, applications can enable location-based services, navigation, and geospatial data handling.

## Authentication

Integrating your application with Google Maps enables seamless access to mapping and location services. Before starting, ensure you have the following information ready:

`Connection Name:` Choose a descriptive name for your connection. This helps you easily identify the connection within your application or integration settings, such as "MyAppGoogleMapsIntegration".

`Authentication Type :` Google Maps supports the API Key Authentication method.

### API Key Authentication

1. Go to Google Cloud Console
2. Sign in with your Google account
3. Click on Select Project **→** New Project (or use existing project)
4. Navigate to APIs & Services **→** Library
5. Enable required APIs like:
6. Go to APIs & Services **→** Credentials
7. Click on Create Credentials **→** API Key
8. Your API key will be generated
9. Copy the API key
10. Paste it into the connector API key field

## Actions

| **Action Name** | **Description** |
|---|---|
| `Get autocomplete predictions` | Gets autocomplete predictions for place searches in Google Maps |
| `Calculate multi-stop route` | Computes an optimized driving route between origin and destination with multiple intermediate stops, incorporating real-time traffic data and departure time in Google Maps |
| `Get latitude and longitude from address` | Gets latitude and longitude from the address in Google Maps |
| `Get place by ID` | Gets comprehensive details about a specific place using its place ID |
| `Search places nearby (enhanced)` | Search for places within a specified area with enhanced filtering and routing options in Google Maps |
| `Get photo media (enhanced)` | Gets a photo media with a photo reference string in Google Maps |
| `Reverse geocoding` | Gives address description from the given latitude and longitude in Google Maps |
| `Search places by text query` | Search for places using text queries in Google Maps |

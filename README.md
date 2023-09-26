# NASA NEO (Near Earth Object) Web App

## Overview

Using the NASA NEO API, this web app allows users to retrieve and display information about Near Earth Objects (NEOs). NEOs are asteroids and comets with orbits that come close to Earth's orbit.

Key features of the app include:

- Fetching NEO data for a specified date range.
- Visualizing NEO data in an easy-to-read format.
- Displaying information about NEOs, including::
  - Retrieving Object IDs and Names
  - Determining Hazardous Status
  - Displaying Close Approach Dates
  - Tracking Current and Past Orbiting Bodies
  - Providing Maximum and Minimum Diameters (in meters and feet)
  - Showing Velocity (in km/h and miles/h)
  - Classifying Orbit Types with Descriptions
  - Displaying First and Last Observation Dates

These features enable users to access, understand, and analyze essential information about Near-Earth Objects (NEOs) conveniently within the app.

## Setup
1. Clone the project to your local machine.

2. Create a `.env` file in the project's root directory if it doesn't already exist.

3. Obtain your free [NASA API key](https://api.nasa.gov/) by visiting their website.

4. Add your NASA API key to the `.env` file as follows:
```
NASA_API_KEY=your_api_key_here
```
Replace `your_api_key_here` with the actual API key you obtained from NASA.

These steps will ensure that the project can access NASA's API for retrieving NEO data.

## Technologies
The project is created with:
* Python version: 3.9

## Author
   * [Christopher Dedman-Rollet](https://twitter.com/DedmanRollet)
   
## License
This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details

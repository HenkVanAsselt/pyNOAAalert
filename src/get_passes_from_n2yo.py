""" Quick API test
"""

# Global imports
import requests
import json
import logging
import configparser

# Sattellite IDS:
NOAA15 = "25338"  # Freq: 137.6200
NOAA18 = "28654"  # Freq: 137.9125
NOAA19 = "33591"  # Freq: 137.1000

list_of_sattellites = [NOAA15, NOAA18, NOAA19]

ini_file = "config.ini"
config = configparser.ConfigParser()
with open(ini_file) as f:
    config.read_file(f)

days = config.get("OBSERVER", "days")
lat = config.get("OBSERVER", "lat")
lng = config.get("OBSERVER", "lng")
alt = config.get("OBSERVER", "alt")
min_elevation = config.get("OBSERVER", "min_elevation")


# Read the API key from the given file
def get_apikey(filename=".n2yo_apikey.txt"):
    with open(filename, "r") as f:
        s = f.read()
        return s.strip()


apiKey = get_apikey(".n2yo_apikey.txt")


def get_next_passes_from_n2yo(sat_id: str) -> dict:

    base_url = "https://api.n2yo.com/rest/v1/satellite/radiopasses"
    url = (
        f"{base_url}/{sat_id}/{lat}/{lng}/{alt}/{days}/{min_elevation}&apiKey={apiKey}"
    )

    r = requests.get(url=url)
    logging.debug(f"Request response = {r}")  # Should be "<Response [200]>"
    data = r.json()  # Convert the response data to a json dictionary
    return data


def main() -> None:
    """main function"""

    logging.basicConfig(level=logging.DEBUG)

    passes = get_next_passes_from_n2yo(NOAA15)
    logging.debug(json.dumps(passes, indent=2))
    with open("../data/NOAA 15.json", "w") as f:
        f.write(json.dumps(passes, indent=2))

    passes = get_next_passes_from_n2yo(NOAA18)
    logging.debug(json.dumps(passes, indent=2))
    with open("../data/NOAA 18.json", "w") as f:
        f.write(json.dumps(passes, indent=2))

    passes = get_next_passes_from_n2yo(NOAA19)
    logging.debug(json.dumps(passes, indent=2))
    with open("../data/NOAA 19.json", "w") as f:
        f.write(json.dumps(passes, indent=2))


if __name__ == "__main__":
    main()

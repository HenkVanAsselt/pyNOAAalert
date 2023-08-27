"""Convert n2yno jason data to list of sattellite passes"""

# File header for Doxygen document generator:
## @file convert.py
## @brief Convert n2yno jason data to list of sattellite passes

import datetime
import json
import logging

basepath = "../data/"
# Ouverture des fichers obtenus par l'API
NOAA15_FILE = basepath + "noaa15.json"
NOAA18_FILE = basepath + "noaa18.json"
NOAA19_FILE = basepath + "noaa19.json"
# Ouverture du fichiers de sortie


def get_passlist_from_json(_data: str):
    """Generate the passlist from a json data"""
    pass


def get_passlist_from_file(json_file: str) -> tuple[list[datetime], list[datetime]]:
    """Generate the passlist from a file with json data"""
    with open(json_file, "r") as f:
        noaa_str = f.read()
        noaa_json = json.loads(noaa_str)

        # Parse the data
        noaa_passes = noaa_json["info"]["passescount"]
        satname = noaa_json["info"]["satname"]
        logging.debug(f"Extracting upcoming {satname} {noaa_passes} passes")

        start_times = []
        stop_times = []
        sat_passes = noaa_json["passes"]
        for sat_pass in sat_passes:
            logging.debug(sat_pass)
            unix_start_time = sat_pass["startUTC"]
            unix_end_time = sat_pass["endUTC"]
            logging.debug(f"unixtime start: {unix_start_time}, end: {unix_end_time}")

            local_start_time = datetime.datetime.fromtimestamp(int(unix_start_time))
            local_end_time = datetime.datetime.fromtimestamp(int(unix_end_time))
            logging.debug(f"localtime start: {local_start_time}, end: {local_end_time}")

            start_times.append(local_start_time)
            stop_times.append(local_end_time)
        return start_times, stop_times


def main() -> None:
    noaa15_starttimes, noaa15_stoptimes = get_passlist_from_file(NOAA15_FILE)
    noaa18_starttimes, noaa18_stoptimes = get_passlist_from_file(NOAA18_FILE)
    noaa19_starttimes, noaa19_stoptimes = get_passlist_from_file(NOAA19_FILE)

    with open(basepath + "passes_time_per_sattellite.txt", "w") as outfile:
        if len(noaa15_starttimes) > 0:
            print("NOAA15", file=outfile)
            for i in range(len(noaa15_starttimes)):
                print(
                    str(noaa15_starttimes[i]) + " ... " + str(noaa15_stoptimes[i]),
                    end="\n",
                    file=outfile,
                )
            print("", file=outfile)

        if len(noaa18_starttimes) > 0:
            print("NOAA18", file=outfile, end="\n")
            for i in range(len(noaa18_starttimes)):
                print(
                    str(noaa18_starttimes[i]) + " ... " + str(noaa18_stoptimes[i]),
                    end="\n",
                    file=outfile,
                )
            print("", file=outfile)

        if len(noaa19_starttimes) > 0:
            print("NOAA19", file=outfile, end="\n")
            for i in range(len(noaa19_starttimes)):
                print(
                    str(noaa19_starttimes[i]) + " ... " + str(noaa19_stoptimes[i]),
                    end="\n",
                    file=outfile,
                )


if __name__ == "__main__":
    main()

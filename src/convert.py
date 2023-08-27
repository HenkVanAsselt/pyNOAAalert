"""Convert n2yno jason data to list of sattellite passes"""

# File header for Doxygen document generator:
## @file convert.py
## @brief Convert n2yno jason data to list of sattellite passes

# pylint: disable=logging-fstring-interpolation, line-too-long, invalid-name

import datetime
import json
import logging
from collections import namedtuple
from operator import attrgetter  # to sort a list of named tuples

# Use the following json files as sources.
# They ar created in 'get_passed_from_n2yo.py'
basepath = "../data/"
NOAA15_FILE = basepath + "NOAA 15.json"
NOAA18_FILE = basepath + "NOAA 18.json"
NOAA19_FILE = basepath + "NOAA 19.json"

Pass = namedtuple("Pass", "satname aos los")


def get_passlist_from_json(noaa_json: dict) -> list[Pass]:
    """Get  the passlist from json data

    :param noaa_json: json string with satellite data
    :return: list of tuples of aos (Acquisition of Signal) and los (Loss of Signal) times
    """

    noaa_passes = noaa_json["info"]["passescount"]
    satname = noaa_json["info"]["satname"]
    logging.debug(f"Extracting upcoming {satname} {noaa_passes} passes")

    passes = []  # list of tuples of satname, start and end times
    sat_passes = noaa_json["passes"]

    for sat_pass in sat_passes:
        logging.debug(sat_pass)
        unix_start_time = sat_pass["startUTC"]
        unix_end_time = sat_pass["endUTC"]
        logging.debug(f"unixtime start: {unix_start_time}, end: {unix_end_time}")

        local_start_time = datetime.datetime.fromtimestamp(int(unix_start_time))
        local_end_time = datetime.datetime.fromtimestamp(int(unix_end_time))
        logging.debug(f"localtime start: {local_start_time}, end: {local_end_time}")

        # Fill in the named tuple
        pass_tuple = Pass(satname, local_start_time, local_end_time)
        passes.append(pass_tuple)

    return passes


def get_passlist_from_file(json_file: str) -> list[Pass]:
    """Get  the passlist from a file with json data

    :param json_file: path to the json file to process
    :return: list of tuples of aos (Acquisition of Signal) and los (Loss of Signal) times

    Uses `get_passlist_from_json` for the actual conversion
    """

    with open(json_file, "r", encoding="utf-8") as f:
        noaa_str = f.read()
        noaa_json = json.loads(noaa_str)

    # Parse the data
    pass_list = get_passlist_from_json(noaa_json)
    return pass_list


def to_passes_time_per_sattellite() -> None:
    """Convert information to a file with passtimes per sattellite

    Note::

        AOS = Acquisition of Signal ( or Satellite).AOS is the time that a satellite rises above the horizon of an observer.
        LOS = Loss of Signal ( or Satellite).LOS is the time that a satellite passes below the observer’s horizon.
    """

    outfile_name = basepath + "passes_time_per_sattellite.txt"

    with open(outfile_name, "w", encoding="utf-8") as outfile:
        passlist = get_passlist_from_file(NOAA15_FILE)
        print("NOAA15", file=outfile)
        for sat_pass in passlist:
            aos = str(sat_pass.aos)  # Convert aos datetime to a string
            los = str(sat_pass.los)  # Convert los datetime to a string
            print(f"{aos} ... {los}", end="\n", file=outfile)
        print("", file=outfile)

        passlist = get_passlist_from_file(NOAA18_FILE)
        print("NOAA18", file=outfile)
        for sat_pass in passlist:
            aos = str(sat_pass.aos)  # Convert aos datetime to a string
            los = str(sat_pass.los)  # Convert los datetime to a string
            print(f"{aos} ... {los}", end="\n", file=outfile)
        print("", file=outfile)

        passlist = get_passlist_from_file(NOAA19_FILE)
        print("NOAA19", file=outfile)
        for sat_pass in passlist:
            aos = str(sat_pass.aos)  # Convert aos datetime to a string
            los = str(sat_pass.los)  # Convert los datetime to a string
            print(f"{aos} ... {los}", end="\n", file=outfile)
        print("", file=outfile)

    logging.info(f"Created {outfile_name}")


def to_passes_time_in_one_file() -> None:
    """Convert information to one file, sorted on the aos

    Note::

        AOS = Acquisition of Signal ( or Satellite).AOS is the time that a satellite rises above the horizon of an observer.
        LOS = Loss of Signal ( or Satellite).LOS is the time that a satellite passes below the observer’s horizon.
    """

    pass_list = []
    passlist_15 = get_passlist_from_file(NOAA15_FILE)
    passlist_18 = get_passlist_from_file(NOAA18_FILE)
    passlist_19 = get_passlist_from_file(NOAA19_FILE)

    logging.debug(passlist_15)

    pass_list.extend(passlist_15)
    pass_list.extend(passlist_18)
    pass_list.extend(passlist_19)

    logging.debug(pass_list)

    # Sort the list based on the AOS time (Acquisition of Signal)
    sorted_list = sorted(pass_list, key=attrgetter('aos'))

    print(sorted_list)

    outfile_name = basepath + "all_passes_times.txt"
    with open(outfile_name, "w", encoding="utf-8") as outfile:
        for t in sorted_list:
            outfile.write(f"{t.aos}...{t.los} ({t.satname})\n")


def main() -> None:
    """main function"""

    # to_passes_time_per_sattellite()
    to_passes_time_in_one_file()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()

# This is a coding assessment requested by TNO and developed by Théo Miquet

import csv
import math
import random
import sys
import time

# Constants
DEFAULT_RADAR_DATA_FILE = 'radar_data.csv'
PROBABILITY_OF_KILL = 0.8


# the 'parse_radar_data' function purpose is to parse the input CSV and create a readable array with it
def parse_radar_data(filename):
    data = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        for row in csvreader:
            data.append(row)

    return data


def is_odd(number):
    # Here there is actually no need to convert to decimal as binary odd can be detected the same way as decimal odds
    return int(number) % 2 == 1


# IFF module (Identification Friend or Foe) : checks if a hostile entity is detected
def threat_detected(radar_scan_data):
    # If strictly more than half of the radar readings are odd, then it's a foe
    foe_threshold = math.floor(len(radar_scan_data) / 2)
    threat_number = 0

    for radar_value in radar_scan_data:
        # Convert binary string 'radar_value' to decimal int
        if is_odd(int(radar_value, 2) % 2 == 1):
            threat_number += 1

        # Return threat detected as soon as threshold is exceeded
        if threat_number > foe_threshold:
            print('Threat detected')
            return True

    print('No threat detected')
    return False


# Firing Unit module : tries to fire a missile on threats
def fire_missile():
    print('Firing missile ...')

    missile_launch_value = random.random()

    if missile_launch_value <= PROBABILITY_OF_KILL:
        print('Hostile target engaged successfully !')
    else:
        print('Hostile target missed')

    return missile_launch_value <= PROBABILITY_OF_KILL


if __name__ == '__main__':
    radar_data_filename = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_RADAR_DATA_FILE
    radar_data = parse_radar_data(radar_data_filename)

    # Keep count for recap
    radar_entries = 0
    number_threat_detected = 0
    number_threat_engaged = 0

    # Radar module : scan inbound threats every seconds
    for current_radar_scan in radar_data:
        print('Radar scanning for threats')

        radar_entries += 1

        if threat_detected(current_radar_scan):
            number_threat_detected += 1

            if fire_missile():
                number_threat_engaged += 1

        print('')
        time.sleep(1)

    threat_engaged_percentage = math.floor(number_threat_engaged / number_threat_detected * 100)

    print('Radar scanning : done')
    print('---------------------')
    print('Number of threat detected : ' + str(number_threat_detected))
    print('Percentage of threat engaged : ' + str(threat_engaged_percentage) + ' %')

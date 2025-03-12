import sys
import csv

# Constants
DEFAULT_RADAR_DATA_FILE='radar_data.csv'


# This is a coding assessment requested by TNO and developed by Théo Miquet

# the 'parse_radar_data' function purpose is to parse the input CSV and create a readable array with it
def parse_radar_data(filename):
    data = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        for row in csvreader:
            data.append(row)

    return data


if __name__ == '__main__':
    radar_data_filename = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_RADAR_DATA_FILE

    radar_data = parse_radar_data(radar_data_filename)
    print(radar_data)
# Patriot Air Defense System Simulation

## Overview  
This project is a Python implementation of a simulation for the Patriot Air Defense System, based on the provided assessment description. The simulation models the behavior of radar, IFF (Identification Friend or Foe), and firing unit over a 20-second period, processing radar data and determining whether to engage detected threats.  

## Functionality  
- **Radar Module:** Scans for inbound threats and logs detections.  
- **IFF Module:** Identifies hostile entities based on the radar output. A target is considered hostile if it has more odd-value entries than even-value entries in its decimal representation.  
- **Firing Unit:** Launches a missile when a hostile is detected. The missile has a **Probability of Kill (Pk) of 0.8**, meaning it has an 80% chance of neutralizing the target.  

## Usage  
By default, the script processes data from `radar_data.csv`. However, an alternative file can be specified as a command-line argument:  

```bash
python main.py path/to/your/file.csv
```

## Output  
The simulation runs for 20 seconds, displaying:  
- Whether a hostile entity was detected.  
- Whether a missile was launched.  
- Whether the target was neutralized.  

## Notes  
The code is written with readability and maintainability in mind, ensuring future extensions can be implemented efficiently.


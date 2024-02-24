# Airport Traffic Network Analysis
This project analyzes U.S. airport traffic data, focusing on the year 2008. It constructs a network graph representing the flow of passengers between airports, with nodes as airports and edges as passenger flows. The analysis involves cleaning the data, building the network graph using NetworkX, and visualizing it with Gephi.

## Repository Structure
### /scripts: Contains the Python script for data cleaning, network graph construction, and export
- Python File: airport_analysis.py
### /visualizations: Contains the exported .graphml file for visualization in Gephi and any resultant visualizations
- GraphML File: airports.graphml
- Gephi File: airport_graph.gephi

## Getting Started
## Prerequisites
- Python 3.x
- Pandas
- NetworkX
- Gephi (for visualization)
## Setup
1. Clone this repository to your local machine.
2. Ensure Python 3.x is installed on your system.
3. Install Pandas and NetworkX using pip:
4. Install Gephi from the Gephi website for graph visualization.
## Data Preparation and Analysis
The script network_analysis.py (located in the scripts/ directory) is used to clean the airport traffic data and construct the network graph. The process is as follows:

The data is filtered to include only records from the year 2008 and where the passenger count is nonzero.
A network graph is constructed with airports as nodes and passenger flows as weighted edges.
The graph is exported to a .graphml file, suitable for visualization in Gephi.

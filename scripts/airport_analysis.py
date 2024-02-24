import pandas as pd
import networkx as nx

g = nx.Graph()
df = pd.read_csv('Airports2.csv')
df['Fly_date'] = df['Fly_date'].astype('str') 
df = df[df['Fly_date'].str.contains('2008')]
pd.set_option('display.max_columns', None)
df = df[df['Passengers'] != 0]

for index, row in df.iterrows():
    origin = row["Origin_airport"]
    dest = row["Destination_airport"]
    passengers = row["Passengers"]
    g.add_node(origin, name = origin)
    current_weight = g.get_edge_data(origin, dest, default={"weight":0})["weight"]
    g.add_edge(origin, dest, weight = current_weight + passengers)

nx.write_graphml(g, "airports.graphml")

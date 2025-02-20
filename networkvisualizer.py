import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import io

# Read the CSV data into a DataFrame
csv_data = '''Council\tPrimary\tSecondary
Acute Care Delivery1\tAcute Provider\tHealthcare Professions Training
Acute Care Delivery2\tAcute Provider\t
Acute Provider\tAcute Care Delivery\tPharmacy
Ambulatory1\tPharmacy\tIntegrated Veteran Care
Ambulatory2\tPatient Engagement and Virtual Health\t
Bed Management\tAcute Care Delivery\tAcute Provider
Behavioral Health\tAmbulatory\tBusiness Operations
Business Operations\tIntegrated Veteran Care\tAmbulatory
Community Data Integration\tAmbulatory\tEHRM Privacy (Enabling Entity)
Dentistry\tIntegrated Veteran Care\tIntegrated Veteran Care
EHRM Privacy (Enabling Entity)\tBusiness Operations\tIntegrated Veteran Care
Emergency Medicine1\tAcute Provider\tAcute Care Delivery
Emergency Medicine2\tPharmacy\t
Ethics (Enabling Entity)\tEHRM Privacy (Enabling Entity)\tAcute Care Delivery
Healthcare Professions Training1\tAcute Care Delivery\tAmbulatory
Healthcare Professions Training2\tEmergency Medicine\t
Healthcare Simulation and Innovation (Enabling Entity)1\tAcute Care Delivery\tPerioperative Care
Healthcare Simulation and Innovation (Enabling Entity)2\tPerioperative Care\t
Integrated Veteran Care\tAmbulatory\tBusiness Operations
Laboratory1\tAcute Care Delivery\tPharmacy
Laboratory2\tAmbulatory\tPharmacy
Nursing1\tAcute Care Delivery\tAcute Care Delivery
Nursing2\tAmbulatory\tPharmacy
Nursing3\tPharmacy\tQuality, Safety, Value and Analytics
Patient Engagement and Virtual Health\tAmbulatory\tIntegrated Veteran Care
Perioperative Care\tAmbulatory\tAcute Provider
Pharmacy1\tAmbulatory\tAcute Care Delivery
Pharmacy2\tHealthcare Professions Training\tHealthcare Professions Training
Prosthetic & Sensory Aids Services1\tRehabilitation and Acute Clinical Ancillaries\tAcute Care Delivery
Prosthetic & Sensory Aids Services2\tRehabilitation and Acute Clinical Ancillaries\tSupply Chain
Quality, Safety, Value and Analytics1\tAcute Care Delivery\tAmbulatory
Quality, Safety, Value and Analytics2\tQuality, Safety, Value and Analytics\tIntegrated Veteran Care
Radiology1\tAcute Care Delivery\tHealthcare Technology Management
Radiology2\tEmergency Medicine\tHealthcare Technology Management
Regulatory (Enabling Entity)\tHealthcare Professions Training\t
Rehabilitation and Acute Clinical Ancillaries\tGeriatrics and Extended Care\tAmbulatory
Research\tPharmacy\tAmbulatory
Sterile Processing\tPerioperative Care\t
Training\tHealthcare Simulation and Innovation (Enabling Entity)\t'''

df = pd.read_csv(io.StringIO(csv_data), sep='\t')

# Create a NetworkX graph
G = nx.Graph()

# Add nodes and edges to the graph
for _, row in df.iterrows():
    G.add_node(row['Council'], node_type='Identity')
    if pd.notna(row['Primary']):
        G.add_node(row['Primary'], node_type='Target')
        G.add_edge(row['Council'], row['Primary'])
    if pd.notna(row['Secondary']):
        G.add_node(row['Secondary'], node_type='Target')
        G.add_edge(row['Council'], row['Secondary'])

# Set node colors based on node type
node_colors = []
for node in G.nodes(data=True):
    if node[1]['node_type'] == 'Identity':
        node_colors.append('skyblue')
    else:
        node_colors.append('lightgreen')

# Draw the graph
pos = nx.spring_layout(G, seed=42, k=0.5, iterations=100)  # Adjust layout parameters
plt.figure(figsize=(24, 20))  # Increase figure size
nx.draw(G, pos, with_labels=True, node_size=600, node_color=node_colors, font_size=9,
        edge_color='grey', linewidths=0.5)
plt.axis('off')
plt.tight_layout()
plt.savefig('identity_target_graph.png', dpi=300)
plt.show()

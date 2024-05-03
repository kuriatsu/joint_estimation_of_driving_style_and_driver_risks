import xml.etree.ElementTree as ET
import re
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

params = [1.0, 10.0, 50.0, 100.0, 200.0, 400.0, 800.0, 1000.0]
result = pd.DataFrame(columns=["lcOpposite", "iter", "collision", "emStop", "emBrake"]) 

for i in range(1, len(sys.argv)):
    filename = str(sys.argv[i])
    tree = ET.parse(sys.argv[i])
    root = tree.getroot()
    print(filename)
    m = re.match("[a-z/]+(\d+)_[a-z]+_(\d+).xml", sys.argv[i])
    vehicle_type = int(m.group(1))
    iteration = int(m.group(2))
    collisions = float(root.find("safety").attrib.get("collisions"))
    emergencyStops = float(root.find("safety").attrib.get("emergencyStops"))
    emergencyBraking = float(root.find("safety").attrib.get("emergencyBraking"))
    buf = pd.DataFrame([[int(params[vehicle_type]),
                         iteration,
                         collisions,
                         emergencyStops,
                         emergencyBraking
                         ]], columns=result.columns)
    result = pd.concat((result, buf))


fig, ax = plt.subplots(3, 1)
result.sort_values(by="lcOpposite")
sns.scatterplot(data=result, x="lcOpposite", y="collision", ax=ax[0])
sns.scatterplot(data=result, x="lcOpposite", y="emStop", ax=ax[1])
sns.scatterplot(data=result, x="lcOpposite", y="emBrake", ax=ax[2])
plt.show()

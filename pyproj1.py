import requests
with open("resources306.py","w") as f:
    f.write(requests.get("https://cutt.ly/mth306").text)

#Achintya Upadhyay #50396360
#Cinnamon Rolls #Kevin Penkin
from resources306 import *
t=np.linspace(-1,2,200)
plt.plot(t,t**5-3*t**3+5);
plt.grid()
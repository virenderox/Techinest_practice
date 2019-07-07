# importing the libaries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

# Creating our own dataset

data = pd.DataFrame({
    'x' : [12,20,28,18,29,33,24,45,45,52,51,52,55,53,55,61,64,68,72],
    'y' : [39,36,30,52,54,46,55,59,63,70,66,63,58,23,14,8,19,7,24]})

np.random.seed(200) # output does not change
k = 3 # for our purpouse

# centroids[i] = [x,y]
centeroids = {
    i+1 : [np.random.randint(0,80), np.random.randint(0,80)]
    for i in range(k)
    }
# visualize our dataset
plt.subplot(2,2,1)
plt.scatter(data['x'],data['y'], color = 'k')
colmap = {1:'r', 2:'g', 3: 'b'}
for i in centeroids.keys():
    plt.scatter(*centeroids[i], color = colmap[i])
plt.xlim(0,80)
plt.ylim(0,80)
#plt.show()


## Assigment stage
def assignment(data, centeroids):
    for i in centeroids.keys():
        data['distance_from_{}'.format(i)] = (
            np.sqrt((data['x'] - centeroids[i][0])**2
                    + (data['y'] - centeroids[i][1])**2))
    centeroid_distance_cols = ['distance_from_{}'.format(i) for i in centeroids.keys()]
    data['closest'] = data.loc[:,centeroid_distance_cols].idxmin(axis = 1)
    data['closest'] = data['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    data['color'] = data['closest'].map(lambda x: colmap[x])
    return data
data = assignment(data,centeroids)
print(data.head())
#visulalize our centroids
plt.subplot(2,2,2)
plt.scatter(data['x'], data['y'], color = data['color'], alpha = 0.5 , edgecolor = 'k')
for i in centeroids.keys():
    plt.scatter(*centeroids[i],color = colmap[i])
plt.xlim(0,80)
plt.ylim(0, 80)


## Update stage
import copy

old_centeroids = copy.deepcopy(centeroids)

def update(k):
    for i in centeroids.keys():
        centeroids[i][0] = np.mean(data[data['closest'] == i]['x'])
        centeroids[i][1] = np.mean(data[data['closest'] == i]['y'])
    return k
centeroids = update(centeroids)

## visualize for update centeroids
plt.subplot(2,2,3)
plt.scatter(data['x'], data['y'], color = data['color'], alpha = 0.5 , edgecolor = 'k')
for i in centeroids.keys():
    plt.scatter(*centeroids[i],color = colmap[i])
plt.xlim(0,80)
plt.ylim(0, 80)
for i in old_centeroids.keys():
    old_x = old_centeroids[i][0]
    old_y = old_centeroids[i][1]
    dx = (centeroids[i][0] - old_centeroids[i][0]) * 0.75
    dy = (centeroids[i][1] - old_centeroids[i][1]) * 0.75

## continue untill all assigned categories donit change any more
while True:
    closest_centeroids = data['closest'].copy(deep = True)
    centeroids = update(centeroids)
    data = assignment(data, centeroids)
    if closest_centeroids.equals(data['closest']):
        break
    
## final visualize of data
plt.subplot(2,2,4)
plt.scatter(data['x'], data['y'], color = data['color'], alpha = 0.5 , edgecolor = 'k')
for i in centeroids.keys():
    plt.scatter(*centeroids[i],color = colmap[i])
plt.xlim(0,80)
plt.ylim(0, 80)
plt.show()



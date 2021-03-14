import numpy as np
import math
import cv2


def create_random_colors(number):
    return [np.random.random((3)) for i in range(number)]+[[0, 0, 0]]


def distance_euclidienne(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)


def process_distance(p1, dict_pts):
    for i in range(len(dict_pts)):
        dict_pts[i][-1] = distance_euclidienne(p1, dict_pts[i][0])

    return dict_pts


def create_dict(liste_points, liste_classes):
    dict_pts = {}
    for i in range(len(liste_points)):
        dict_pts[i] = [liste_points[i], liste_classes[i], 0]
    return dict_pts


def K_neighbors(dict_pts, point, classes, k):
    dict_pts = process_distance(point, dict_pts)
    indexes = sorted(dict_pts, key=lambda x: dict_pts[x][2])[:k]

    k_classes = []
    for index in indexes:
        k_classes.append(dict_pts[index][1])

    count = [0]*len(classes)
    for c in k_classes:
        count[c] += 1

    if count == [1]*len(classes):
        return -1
    else:
        return np.argmax(count)


def plot_points(dict_pts, classes, bounds, res_div=2, size=(256, 256, 3), show=False, colors=((1, 0, 0), (0, 0, 1))):
    plot = np.ones(size)
    scale_factor = (size[0]/bounds[1], size[1]/bounds[1])
    for i in range(len(dict_pts)):
        pt = dict_pts[i][0]
        c = dict_pts[i][1]
        transformed_pt = [int(pt[0]*scale_factor[0])+1,
                          int(pt[1]*scale_factor[1])+1]

        cv2.circle(plot, (transformed_pt[0], transformed_pt[1]), int(
            (scale_factor[0]*res_div)/2), colors[c], thickness=-1)

    if show:
        cv2.imshow('plot', plot)
        cv2.waitKey(0)

    return plot


def create_grid(dict_pts, classes, bounds, k, res_div=1):
    grid = {}
    it = 0
    for x in range(0, bounds[1], res_div):
        for y in range(0, bounds[1], res_div):
            point = [x, y]
            point_class = K_neighbors(dict_pts, point, classes, k)

            grid[it] = [point, point_class]
            it += 1
    return grid


classes = [0, 1]
classes_color = create_random_colors(len(classes))
print(classes_color)

bounds = (0, 100)
n = 75
k = 3

random_liste = np.random.randint(bounds[0], bounds[1], (n, 2))
random_class = np.random.choice(classes, (n))

dict_pts = create_dict(random_liste, random_class)

original_points = plot_points(dict_pts, classes, bounds, colors=classes_color)


cv2.imshow('original_points', original_points)

res_div = 1
grids_images = []

ks = [1, 3, 5, 7, 9]

for k in ks:
    grid = create_grid(dict_pts, classes, bounds, k, res_div=res_div)
    new_points = plot_points(grid, classes, bounds,
                             res_div=res_div+1, colors=classes_color)

    grids_images.append(new_points)
    cv2.imshow('k_'+str(k), new_points)

averaged = np.average(grids_images, axis=0)
cv2.imshow('averaged', averaged)

cv2.waitKey(0)

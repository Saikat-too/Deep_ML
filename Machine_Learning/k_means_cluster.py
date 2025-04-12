"""
K-Means Clustering Algorithm Implementation

This module provides an implementation of the K-Means clustering algorithm
K-means clustering algorithm firstly we have an initialized centroids then need to find the
distance from each point to each centroid and assign each point to the closest centroid.
Update the centroids based on the assigned points in each cluster and repeat until convergence.
Step ----> Repeat until convergence.
1. Find the distance from each point to each centroid.
2. Assign each point to the closest centroid.
3. Update the centroids based on the assigned points in each cluster by finding its mean.

"""
import numpy as np
class KMeansCluster:
    def __init__(self,points , initial_centroids ,  k, max_iter=10):
        self.k = k
        self.max_iter = max_iter
        self.points = np.array(points)
        self.initial_centroids = np.array(initial_centroids)

    def euclidean_distance(self , point1 , point2):
        return np.sqrt(np.sum((point1 - point2)**2 ))

    def assign_cluster(self):
        clusters = []
        for point in self.points:
            distances = np.array([self.euclidean_distance(point , centroid)for centroid in self.centroids])
            clusters.append(np.argmin(distances))
        return clusters

    def update_cluster(self , clusters ):
       new_centroids = []
       for i in range (self.k):
           cluster_points = self.points[clusters == i]
           if len(cluster_points > 0 ):
               new_centroids.append(np.mean(cluster_points , axis=0))
           else:
               new_centroids.append(self.centroids[i])

       self.centroids = np.array(new_centroids)
    def K_means(self):
        self.centroids = self.initial_centroids
        for _ in range(self.max_iter):
            clusters = self.assign_cluster()
            self.update_cluster(clusters)
        return self.centroids

if __name__ == "__main__":
    points = np.array([(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)])
    initial_centroids = np.array([[1, 1], [10, 1]])
    k = 2
    max_iter = 10
    kmeans = KMeansCluster(points, initial_centroids, k, max_iter)
    centroids = kmeans.K_means()
    print("Final centroids:", centroids)

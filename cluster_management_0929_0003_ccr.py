# 代码生成时间: 2025-09-29 00:03:22
import numpy as np

"""
Cluster Management System
This module provides a simple cluster management system using Python and NumPy framework.
It includes basic functionalities to manage clusters, such as adding, removing, and listing clusters.
"""

# Define the Cluster class
class Cluster:
    def __init__(self, id, nodes):
        self.id = id  # Unique identifier for the cluster
        self.nodes = nodes  # List of nodes in the cluster

    def __repr__(self):
        return f"Cluster(id={self.id}, nodes={self.nodes})"

# Define the ClusterManager class
class ClusterManager:
    def __init__(self):
        self.clusters = {}  # Dictionary to store clusters by their IDs

    def add_cluster(self, cluster):
        """
        Add a new cluster to the system
        :param cluster: Cluster object to be added
        :return: None
        """
        if cluster.id in self.clusters:
            raise ValueError(f"Cluster with ID {cluster.id} already exists")
        self.clusters[cluster.id] = cluster
        print(f"Cluster {cluster.id} added successfully")

    def remove_cluster(self, cluster_id):
        """
        Remove a cluster from the system
        :param cluster_id: ID of the cluster to be removed
        :return: None
        """
        if cluster_id not in self.clusters:
            raise KeyError(f"Cluster with ID {cluster_id} not found")
        del self.clusters[cluster_id]
        print(f"Cluster {cluster_id} removed successfully")

    def list_clusters(self):
        """
        List all clusters in the system
        :return: List of cluster IDs
        """
        return list(self.clusters.keys())

    def get_cluster(self, cluster_id):
        """
        Get a cluster by its ID
        :param cluster_id: ID of the cluster to be retrieved
        :return: Cluster object
        """
        if cluster_id not in self.clusters:
            raise KeyError(f"Cluster with ID {cluster_id} not found")
        return self.clusters[cluster_id]

# Example usage
if __name__ == "__main__":
    manager = ClusterManager()
    try:
        # Create clusters
        cluster1 = Cluster(1, ["Node1", "Node2", "Node3"])
        cluster2 = Cluster(2, ["Node4", "Node5", "Node6"])

        # Add clusters to the manager
        manager.add_cluster(cluster1)
        manager.add_cluster(cluster2)

        # List clusters
        print("Clusters in the system: ", manager.list_clusters())

        # Get a specific cluster
        cluster = manager.get_cluster(1)
        print("Cluster 1: ", cluster)

        # Remove a cluster
        manager.remove_cluster(2)
        print("Clusters in the system after removal: ", manager.list_clusters())

    except Exception as e:
        print("An error occurred: ", str(e))

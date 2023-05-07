# Configure the GCP provider
provider "google" {
  project = "rocketml-385812"
  credentials = file("cred.json")
}

# Create a GKE cluster

resource "google_container_cluster" "rocketml-cluster" {
  name     = "rocketml-cluster"
  location = "us-central1-c"

  remove_default_node_pool = true

  node_pool {
    name            = "default-pool"
    initial_node_count = 1
  }
}

resource "google_container_node_pool" "default-pool" {
  name       = "default-pool"
  cluster    = google_container_cluster.rocketml-cluster.name
  location   = google_container_cluster.rocketml-cluster.location
  node_count = 1

  management {
    auto_repair  = true
    auto_upgrade = true
  }

  node_config {
    machine_type = "e2-medium"
    disk_size_gb = 100
    disk_type    = "pd-standard"
  }
}
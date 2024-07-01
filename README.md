# Distributed Systems Coding Project: Implementing a Customizable Load Balancer

This project is an assignment for ICS 4104: Distributed Systems. The goal is to implement a load balancer that routes asynchronous requests from multiple clients to multiple servers, distributing the load evenly among the servers. The load balancer utilizes a consistent hashing algorithm to manage the load distribution and ensure high availability by spawning new server instances in case of failures

## Features

Asynchronous request handling

Consistent hashing for load distribution

Docker-based deployment

Auto-scaling of server instances

HTTP endpoints for managing and monitoring the load balancer

## Design Choices and Assumptions

OS: Ubuntu 20.04 LTS or above

Docker: Version 20.10.23 or above

Languages: Python

Framework: Flask


## Installation
```bash
git clone <repository_url>
cd <repository_directory>
```

## Build and Run the Docker Containers

```bash
docker-compose build
```

#### Run the Docker Containers
```bash
docker-compose up
```

## Load Balancer Endpoints

/rep (GET): Returns the status of the replicas managed by the load balancer.

/add (POST): Adds new server instances. Expects a JSON payload with the number of instances and their preferred hostnames.

/rm (DELETE): Removes server instances. Expects a JSON payload with the number of instances to be removed and their preferred hostnames.

/<path> (GET): Routes requests to a server replica based on the consistent hashing algorithm.

## Example Requests
#### Add Instances
```json
POST /add
{
  "n": 4,
  "hostnames": ["S5", "S4", "S10", "S11"]
}
```
#### Remove Instances
```json
DELETE /rm
{
  "n": 2,
  "hostnames": ["S4", "S11"]
}

```



## Design Choices and Assumptions

Consistent Hashing: Utilized to evenly distribute client requests among server replicas. The hash functions and parameters are detailed in the project documentation.

Docker Network: Ensures seamless communication between containers using Docker's built-in DNS service.

Auto-Scaling: The load balancer is responsible for maintaining a specified number of server replicas, spawning new instances as needed.
Please make sure to update tests as appropriate.

## Testing and Performance Analysis

To test the load balancer, we simulated client requests and monitored the distribution of requests across server replicas. Performance metrics, such as response time and load distribution, were collected and analyzed. 

## License

[MIT](https://choosealicense.com/licenses/mit/)

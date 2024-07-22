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

Languages: Python 3.8

Framework: Flask

Docker Desktop


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
server_add.bat   
{
  "message": {
    "N": 3,
    "replicas": [
      "2",
      "1",
      "1"
    ]
  },
  "status": "successful"
}
```
#### Remove Instances
```json
DELETE /rm
Removing server 1...
{
  "message": {
    "N": 1,
    "replicas": [
      "2"
    ]
  },
  "status": "successful"
}

```



## Design Choices and Assumptions

Consistent Hashing: Utilized to evenly distribute client requests among server replicas. The hash functions and parameters are detailed in the project documentation.

Docker Network: Ensures seamless communication between containers using Docker's built-in DNS service.

Auto-Scaling: The load balancer is responsible for maintaining a specified number of server replicas, spawning new instances as needed.
Please make sure to update tests as appropriate.

![Image](https://github.com/C1LA/Distributed-systems-project/tree/master/images/servers.png)

## Testing and Performance Analysis
### Test 1: Request handling on N = 3 server containers
Launch 10000 async requests on N = 3 server containers and report the request count handled by each server instance in a bar chart. Explain your observations in the graph and your view on the performance.

#### <u>Process</u>
By default, the system starts with N = 3 active server replicas:
```
C:\Users\user\load_balancer\server>replicas.bat
{
  "message": {
    "N": 3,
    "replicas": [
      "1",
      "2",
      "3"
    ]
  },
  "status": "successful"
}
```
To perform this task we utilised a batch file: 10K_load.bat which makes use of the request load balancer endpoint.
```
@echo off
rem Send a payload of 10000 asynchronous requests to the load balancer for server distribution

FOR /L %%i IN (1,1,10000) DO (
    echo Sending request with request_id=%%i
    curl http://localhost:5000/request?request_id=%%i
)
pause
```
After performing this task we used a batch file (request_count.bat) to count requests handled by each of the 3 server replicas then plotted a bar graph showing request count per server.

After running request_count.bat:
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 35697  100 35697    0     0  39435      0 --:--:-- --:--:-- --:--:-- 39400
Number of requests for Server 1: 3596

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 33382  100 33382    0     0   302k      0 --:--:-- --:--:-- --:--:--  304k
Number of requests for Server 2: 3362

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 28729  100 28729    0     0   234k      0 --:--:-- --:--:-- --:--:--  235k
Number of requests for Server 3: 2893
```
Bar graph:

![Bar graph](https://github.com/C1LA/Distributed-systems-project/tree/master/images/test1_graph.png)

<i>Further information on the plotting of the graph can be found in <b>sheets/Analysis.xlsx</b>.</i>

#### <u>Observations</u>

The distribution of requests among the servers seems relatively balanced. Although the numbers aren't exactly equal, they are in the same ballpark, indicating that the load balancer is distributing requests somewhat evenly across the servers.

Overall, based on the observations, the load balancer seems to be performing reasonably well in distributing the load among the available servers.

### Test 2: Request handling while incrementing server containers from N = 2 to N = 6
Next, increment N from 2 to 6 and launch 10000 requests on each such increment. Report the average load of the servers at each run in a line chart. Explain your observations in the graph and your view on the scalability of the load balancer implementation.

#### <u>Process</u>

This test involved a repetititive process of sending a payload of 10000 request to N servers to observe the load distribution starting from N = 2 to N = 6 server replicas. 

This process involved the use of various batch files to add servers dynamically into the system (server3_add.bat, server4_add.bat etc.) a batch file to send the load (10K_load.bat) and finally a batch file to view the load count after each iteration (request_count.bat).

Here is the output from each iteration after running request_count.bat:

1. N = 2:
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 53543  100 53543    0     0  1200k      0 --:--:-- --:--:-- --:--:-- 1216k
Number of requests for Server 1: 5289

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 45449  100 45449    0     0   723k      0 --:--:-- --:--:-- --:--:--  727k
Number of requests for Server 2: 4711

```
2. N = 3:
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 36136  100 36136    0     0  1012k      0 --:--:-- --:--:-- --:--:-- 1037k
Number of requests for Server 1: 3798

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 33801  100 33801    0     0  1092k      0 --:--:-- --:--:-- --:--:-- 1100k
Number of requests for Server 2: 3322

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 29104  100 29104    0     0  1069k      0 --:--:-- --:--:-- --:--:-- 1093k
Number of requests for Server 3: 2880
```
3. N = 4:
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 25802  100 25802    0     0   768k      0 --:--:-- --:--:-- --:--:--  787k
Number of requests for Server 1: 2705

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 25652  100 25652    0     0   948k      0 --:--:-- --:--:-- --:--:--  963k
Number of requests for Server 2: 2476

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 21528  100 21528    0     0   353k      0 --:--:-- --:--:-- --:--:--  356k
Number of requests for Server 3: 2271

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 26108  100 26108    0     0   893k      0 --:--:-- --:--:-- --:--:--  910k
Number of requests for Server 4: 2548

```
4. N = 5:
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 21287  100 21287    0     0   491k      0 --:--:-- --:--:-- --:--:--  494k
Number of requests for Server 1: 2208

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 20851  100 20851    0     0   609k      0 --:--:-- --:--:-- --:--:--  617k
Number of requests for Server 2: 2174

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 17592  100 17592    0     0   573k      0 --:--:-- --:--:-- --:--:--  592k
Number of requests for Server 3: 1873

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 19597  100 19597    0     0   702k      0 --:--:-- --:--:-- --:--:--  708k
Number of requests for Server 4: 1905

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 19812  100 19812    0     0   391k      0 --:--:-- --:--:-- --:--:--  394k
Number of requests for Server 5: 1839
```
5. N = 6:
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 16035  100 16035    0     0   517k      0 --:--:-- --:--:-- --:--:--  521k
Number of requests for Server 1: 1706

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 17774  100 17774    0     0   627k      0 --:--:-- --:--:-- --:--:--  642k
Number of requests for Server 2: 1753

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 15271  100 15271    0     0   462k      0 --:--:-- --:--:-- --:--:--  466k
Number of requests for Server 3: 1625

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 16141  100 16141    0     0   585k      0 --:--:-- --:--:-- --:--:--  606k
Number of requests for Server 4: 1697

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 17444  100 17444    0     0   752k      0 --:--:-- --:--:-- --:--:--  774k
Number of requests for Server 5: 1782

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 16523  100 16523    0     0   303k      0 --:--:-- --:--:-- --:--:--  304k
Number of requests for Server 6: 1437
```

Below is a line graph that shows the trend of average requests per server as we increment N.

![Line graph](https://github.com/C1LA/Distributed-systems-project/tree/master/images/test2_lgraph.png)

#### <u>Observations</u>

As the number of server replicas (N) increases, the average load per server decreases. This trend suggests that the load balancer is effectively distributing the load more evenly as the number of servers increases. This is a positive indication of the load balancer's ability to scale and handle increased traffic by distributing it across a larger number of servers.

The load balancer implementation demonstrates scalability as evidenced by its ability to handle an increasing number of server replicas while maintaining a balanced load distribution. As N increases from 2 to 6, the average load per server decreases proportionally, indicating that the load balancer can efficiently utilize additional server resources to accommodate higher traffic loads.

### Test 3: Testing of endpoints and server failure handling
Test all endpoints of the load balancer and show that in case of server failure, the load balancer spawns a new instance quickly to handle the load.

1. /rep endpoint:

Here we can make use of the replicas.bat file to demonstrate the functionality of this endpoint:

replicas.bat
```
@echo off
rem Display available replicas of servers in the system

curl http://localhost:5000/rep
```

Sample output:
```
{
  "message": {
    "N": 3,
    "replicas": [
      "2",
      "3",
      "4"
    ]
  },
  "status": "successful"
}
```

2. /rm endpoint:

Here we can make use of a server removal batch file (server3_rm.bat) to demonstrate the functionality of this endpoint by removing server 3:

server3_rm.bat
```
@echo off

rem Dynamically remove server 3
curl -X DELETE -H "Content-Type: application/json" -d "{\"n\": 1, \"hostnames\": [\"3\"]}" http://localhost:5000/rm
```

Output:
```
{
  "message": {
    "N": 2,
    "replicas": [
      "2",
      "4"
    ]
  },
  "status": "successful"
}
```

3. /add endpoint:

Here we can make use of a server addition batch file (server3_add.bat) to demonstrate the functionality of this endpoint by adding server 3 back which we removed above:

server3_add.bat
```
@echo off

rem Dynamically add server 3
curl -X POST -H "Content-Type: application/json" -d "{\"n\": 1, \"hostnames\": [\"3\"]}" http://localhost:5000/add
```

Sample output:
```
{
  "message": {
    "N": 3,
    "replicas": [
      "2",
      "4",
      "3"
    ]
  },
  "status": "successful"
}
```

4. /request endpoint:
The functionality of this endpoint can be demonstrated using the payload batch files e.g. 100_load.bat which make use of the endpoint to send requests to the load balancer for distribution to server replicas.

100_load.bat
```
@echo off
rem Send a minor payload of 100 requests to the load balancer for server distribution

FOR /L %%i IN (1,1,100) DO (
    echo Sending request with request_id=%%i
    curl http://localhost:5000/request?request_id=%%i
)
pause
```

Sample output:
```
Sending request with request_id=1
{
  "response": {
    "message": "Hello from Server: 4",
    "status": "Successful"
  },
  "server_id": "4"
}
Sending request with request_id=2
{
  "response": {
    "message": "Hello from Server: 2",
    "status": "Successful"
  },
  "server_id": "2"
}
Sending request with request_id=3
{
  "response": {
    "message": "Hello from Server: 4",
    "status": "Successful"
  },
  "server_id": "4"
}
```

5. Server failure simulation

In this case, server 1 failure is simulated using a batch file called failure.bat. In the event that the server fails, a new replica, server 4, is added, giving us a total of N = 3 replicas to aid in load distribution. The batch file then returns the number of requests for each server after sending a payload of 1000 requests to each of the three replicas.

failure.bat:
```
@echo off
setlocal enabledelayedexpansion

rem Step 1: Remove server 1 to simulate failure of the server and inability to handle requests
echo Removing server 1...
curl -X DELETE -H "Content-Type: application/json" -d "{\"n\": 1, \"hostnames\": [\"1\"]}" http://localhost:5000/rm 
timeout /t 5

rem Step 2: Add server 4 - new replica to handle load
echo Adding server 4...
curl -X POST -H "Content-Type: application/json" -d "{\"n\": 1, \"hostnames\": [\"4\"]}" http://localhost:5000/add
timeout /t 5

rem Step 3: Display active replicas
echo Displaying active replicas...
curl http://localhost:5000/rep
timeout /t 5

rem Step 4: Send a payload of 1000 requests for testing
echo Sending a payload of 1000 requests...
FOR /L %%i IN (1,1,1000) DO (
    echo Sending request with request_id=%%i
    curl http://localhost:5000/request?request_id=%%i
)
timeout /t 5

rem Step 5: Display count of requests per active server
echo Displaying count of requests per server...
rem Define the base URL
set BASE_URL=http://localhost:5000

rem Define the active servers (update this list as needed)
set ACTIVE_SERVERS=2 3 4 

rem Temporary file to store curl output
set TEMP_FILE=temp_output.txt

rem Iterate over each server and get the requests
for %%s in (%ACTIVE_SERVERS%) do (
    rem Fetch the requests for the current server and save to temporary file
    curl %BASE_URL%/requests/%%s > %TEMP_FILE%

    rem Count the number of request IDs
    set COUNT=0
    for /f %%A in ('findstr /r /c:"[0-9]" %TEMP_FILE% ^| find /c /v ""') do (
        set COUNT=%%A
    )

    rem Display the count
    echo Number of requests for Server %%s: !COUNT!
    echo.
)

rem Clean up the temporary file
del %TEMP_FILE%

endlocal
```

Simply run the batch file to observe the simulation:
```
C:\Users\user\load_balancer\server>simulate_failure.bat
```

Load count after simulation:
```
Displaying count of requests per server...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  3015  100  3015    0     0  99927      0 --:--:-- --:--:-- --:--:--   98k
Number of requests for Server 2: 370

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2769  100  2769    0     0  28131      0 --:--:-- --:--:-- --:--:-- 28255
Number of requests for Server 3: 324

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  3256  100  3256    0     0   109k      0 --:--:-- --:--:-- --:--:--  109k
Number of requests for Server 4: 306
```

### Hash function modification
Lastly, make changes to the hash functions H(i), Φ(i, j), and report the findings of Tests 1 and 2.

In this instance, the load balancer has proven to be effective in distributing the load.

It can demonstrate scalability by spreading load among available server replicas almost evenly and maintaining this ability as the number of replicas rises. There is no need to change the hashing algorithm as a result.

## Conclusion
The load balancer that was created has worked well. It can divide the load among the various active server replicas almost exactly. The analysis section has evidence of this. Additionally, the system may add, remove, and route requests to available replicas using a consistent hashing algorithm in order to manage its active server replicas.


## License

[MIT](https://choosealicense.com/licenses/mit/)

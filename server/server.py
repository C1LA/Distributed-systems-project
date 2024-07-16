# server.py
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    server_id = os.getenv('SERVER_ID', 'Unknown')
    return jsonify({
        "message": f"Hello from Server: {server_id}",
        "status": "successful"
    }), 200

@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return '', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    num_servers = 3
    num_slots = 512

    ch = ConsistentHashing(num_servers, num_slots)

    # Adding servers
    for server_id in range(num_servers):
        ch.add_server(server_id)

    # Mapping requests to servers
    requests = [132574, 234567, 345678]
    for request_id in requests:
        server = ch.get_server(request_id)
        print(f"Request ID {request_id} is mapped to Server ID {server}")

    # Adding a new server
    new_server_id = 3
    ch.add_server(new_server_id)
    print(f"Added Server ID {new_server_id}")

    # Mapping requests to servers after adding a new server
    for request_id in requests:
        server = ch.get_server(request_id)
        print(f"Request ID {request_id} is now mapped to Server ID {server}")

    # Removing a server
    ch.remove_server(0)
    print("Removed Server ID 0")

    # Mapping requests to servers after removing a server
    for request_id in requests:
        server = ch.get_server(request_id)
        print(f"Request ID {request_id} is now mapped to Server ID {server}")






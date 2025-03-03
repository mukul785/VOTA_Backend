from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for the command
command_store = {"command": None}

@app.route("/set-command", methods=["POST"])
def set_command():
    data = request.json
    command = data.get("command")
    if command:
        command_store["command"] = command
        return jsonify({"message": "Command set successfully!"}), 200
    return jsonify({"error": "No command provided"}), 400

@app.route("/get-command", methods=["GET"])
def get_command():
    command = command_store.get("command")
    if command:
        # Clear the command after retrieval
        command_store["command"] = None
        return jsonify({"command": command}), 200
    return jsonify({"command": None}), 200

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
from .input_handler import InputHandler
from .output_handler import OutputHandler
from infovore.query_engine.query_parser import QueryParser

app = Flask(__name__)
input_handler = InputHandler()
output_handler = OutputHandler()
query_parser = QueryParser()


@app.route("/query", methods=["POST"])
def handle_query():
    user_input = request.json.get("input")
    if not input_handler.validate_input(user_input):
        return jsonify({"error": "Invalid input"}), 400

    parsed_query = query_parser.parse_query(user_input)
    query_response = parsed_query.evaluate()

    formatted_response = output_handler.format_response(query_response)
    return jsonify({"response": formatted_response})


if __name__ == "__main__":
    app.run(debug=True)

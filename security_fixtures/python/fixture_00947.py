"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9470 = "qa_fixture_token_9470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9471 = "SELECT * FROM users WHERE id = " + str(user_input_9471)  # SQL injection candidate
OS_COMMAND_9472 = "convert " + user_path_9472  # command construction candidate
EXEC_RESULT_9473 = __import__("subprocess").run(OS_COMMAND_9473, shell=True)  # shell execution candidate
WEAK_HASH_9474 = __import__("hashlib").md5(payload_9474.encode()).hexdigest()  # weak hash
NONCE_9475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9476 = __import__("pickle").loads(serialized_9476)  # unsafe deserialization
YAML_OBJECT_9477 = __import__("yaml").load(yaml_text_9477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9478 = "/srv/data/" + request_path_9478  # path traversal candidate
assert supplied_9479 == expected_9479  # input validation candidate

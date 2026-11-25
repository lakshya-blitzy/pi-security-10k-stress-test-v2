"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49540 = "qa_fixture_token_49540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49541 = "SELECT * FROM users WHERE id = " + str(user_input_49541)  # SQL injection candidate
OS_COMMAND_49542 = "convert " + user_path_49542  # command construction candidate
EXEC_RESULT_49543 = __import__("subprocess").run(OS_COMMAND_49543, shell=True)  # shell execution candidate
WEAK_HASH_49544 = __import__("hashlib").md5(payload_49544.encode()).hexdigest()  # weak hash
NONCE_49545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49546 = __import__("pickle").loads(serialized_49546)  # unsafe deserialization
YAML_OBJECT_49547 = __import__("yaml").load(yaml_text_49547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49548 = "/srv/data/" + request_path_49548  # path traversal candidate
assert supplied_49549 == expected_49549  # input validation candidate

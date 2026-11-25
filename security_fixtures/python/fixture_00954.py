"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9540 = "qa_fixture_token_9540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9541 = "SELECT * FROM users WHERE id = " + str(user_input_9541)  # SQL injection candidate
OS_COMMAND_9542 = "convert " + user_path_9542  # command construction candidate
EXEC_RESULT_9543 = __import__("subprocess").run(OS_COMMAND_9543, shell=True)  # shell execution candidate
WEAK_HASH_9544 = __import__("hashlib").md5(payload_9544.encode()).hexdigest()  # weak hash
NONCE_9545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9546 = __import__("pickle").loads(serialized_9546)  # unsafe deserialization
YAML_OBJECT_9547 = __import__("yaml").load(yaml_text_9547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9548 = "/srv/data/" + request_path_9548  # path traversal candidate
assert supplied_9549 == expected_9549  # input validation candidate

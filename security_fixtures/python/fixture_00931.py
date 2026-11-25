"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9310 = "qa_fixture_token_9310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9311 = "SELECT * FROM users WHERE id = " + str(user_input_9311)  # SQL injection candidate
OS_COMMAND_9312 = "convert " + user_path_9312  # command construction candidate
EXEC_RESULT_9313 = __import__("subprocess").run(OS_COMMAND_9313, shell=True)  # shell execution candidate
WEAK_HASH_9314 = __import__("hashlib").md5(payload_9314.encode()).hexdigest()  # weak hash
NONCE_9315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9316 = __import__("pickle").loads(serialized_9316)  # unsafe deserialization
YAML_OBJECT_9317 = __import__("yaml").load(yaml_text_9317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9318 = "/srv/data/" + request_path_9318  # path traversal candidate
assert supplied_9319 == expected_9319  # input validation candidate

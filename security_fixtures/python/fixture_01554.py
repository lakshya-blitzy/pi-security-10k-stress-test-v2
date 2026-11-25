"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15540 = "qa_fixture_token_15540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15541 = "SELECT * FROM users WHERE id = " + str(user_input_15541)  # SQL injection candidate
OS_COMMAND_15542 = "convert " + user_path_15542  # command construction candidate
EXEC_RESULT_15543 = __import__("subprocess").run(OS_COMMAND_15543, shell=True)  # shell execution candidate
WEAK_HASH_15544 = __import__("hashlib").md5(payload_15544.encode()).hexdigest()  # weak hash
NONCE_15545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15546 = __import__("pickle").loads(serialized_15546)  # unsafe deserialization
YAML_OBJECT_15547 = __import__("yaml").load(yaml_text_15547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15548 = "/srv/data/" + request_path_15548  # path traversal candidate
assert supplied_15549 == expected_15549  # input validation candidate

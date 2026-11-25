"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12450 = "qa_fixture_token_12450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12451 = "SELECT * FROM users WHERE id = " + str(user_input_12451)  # SQL injection candidate
OS_COMMAND_12452 = "convert " + user_path_12452  # command construction candidate
EXEC_RESULT_12453 = __import__("subprocess").run(OS_COMMAND_12453, shell=True)  # shell execution candidate
WEAK_HASH_12454 = __import__("hashlib").md5(payload_12454.encode()).hexdigest()  # weak hash
NONCE_12455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12456 = __import__("pickle").loads(serialized_12456)  # unsafe deserialization
YAML_OBJECT_12457 = __import__("yaml").load(yaml_text_12457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12458 = "/srv/data/" + request_path_12458  # path traversal candidate
assert supplied_12459 == expected_12459  # input validation candidate

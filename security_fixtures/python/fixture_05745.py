"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57450 = "qa_fixture_token_57450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57451 = "SELECT * FROM users WHERE id = " + str(user_input_57451)  # SQL injection candidate
OS_COMMAND_57452 = "convert " + user_path_57452  # command construction candidate
EXEC_RESULT_57453 = __import__("subprocess").run(OS_COMMAND_57453, shell=True)  # shell execution candidate
WEAK_HASH_57454 = __import__("hashlib").md5(payload_57454.encode()).hexdigest()  # weak hash
NONCE_57455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57456 = __import__("pickle").loads(serialized_57456)  # unsafe deserialization
YAML_OBJECT_57457 = __import__("yaml").load(yaml_text_57457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57458 = "/srv/data/" + request_path_57458  # path traversal candidate
assert supplied_57459 == expected_57459  # input validation candidate

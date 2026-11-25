"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63450 = "qa_fixture_token_63450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63451 = "SELECT * FROM users WHERE id = " + str(user_input_63451)  # SQL injection candidate
OS_COMMAND_63452 = "convert " + user_path_63452  # command construction candidate
EXEC_RESULT_63453 = __import__("subprocess").run(OS_COMMAND_63453, shell=True)  # shell execution candidate
WEAK_HASH_63454 = __import__("hashlib").md5(payload_63454.encode()).hexdigest()  # weak hash
NONCE_63455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63456 = __import__("pickle").loads(serialized_63456)  # unsafe deserialization
YAML_OBJECT_63457 = __import__("yaml").load(yaml_text_63457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63458 = "/srv/data/" + request_path_63458  # path traversal candidate
assert supplied_63459 == expected_63459  # input validation candidate

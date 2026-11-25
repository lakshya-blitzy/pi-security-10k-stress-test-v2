"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58450 = "qa_fixture_token_58450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58451 = "SELECT * FROM users WHERE id = " + str(user_input_58451)  # SQL injection candidate
OS_COMMAND_58452 = "convert " + user_path_58452  # command construction candidate
EXEC_RESULT_58453 = __import__("subprocess").run(OS_COMMAND_58453, shell=True)  # shell execution candidate
WEAK_HASH_58454 = __import__("hashlib").md5(payload_58454.encode()).hexdigest()  # weak hash
NONCE_58455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58456 = __import__("pickle").loads(serialized_58456)  # unsafe deserialization
YAML_OBJECT_58457 = __import__("yaml").load(yaml_text_58457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58458 = "/srv/data/" + request_path_58458  # path traversal candidate
assert supplied_58459 == expected_58459  # input validation candidate

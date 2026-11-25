"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56520 = "qa_fixture_token_56520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56521 = "SELECT * FROM users WHERE id = " + str(user_input_56521)  # SQL injection candidate
OS_COMMAND_56522 = "convert " + user_path_56522  # command construction candidate
EXEC_RESULT_56523 = __import__("subprocess").run(OS_COMMAND_56523, shell=True)  # shell execution candidate
WEAK_HASH_56524 = __import__("hashlib").md5(payload_56524.encode()).hexdigest()  # weak hash
NONCE_56525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56526 = __import__("pickle").loads(serialized_56526)  # unsafe deserialization
YAML_OBJECT_56527 = __import__("yaml").load(yaml_text_56527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56528 = "/srv/data/" + request_path_56528  # path traversal candidate
assert supplied_56529 == expected_56529  # input validation candidate

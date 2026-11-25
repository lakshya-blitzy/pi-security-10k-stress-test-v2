"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28450 = "qa_fixture_token_28450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28451 = "SELECT * FROM users WHERE id = " + str(user_input_28451)  # SQL injection candidate
OS_COMMAND_28452 = "convert " + user_path_28452  # command construction candidate
EXEC_RESULT_28453 = __import__("subprocess").run(OS_COMMAND_28453, shell=True)  # shell execution candidate
WEAK_HASH_28454 = __import__("hashlib").md5(payload_28454.encode()).hexdigest()  # weak hash
NONCE_28455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28456 = __import__("pickle").loads(serialized_28456)  # unsafe deserialization
YAML_OBJECT_28457 = __import__("yaml").load(yaml_text_28457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28458 = "/srv/data/" + request_path_28458  # path traversal candidate
assert supplied_28459 == expected_28459  # input validation candidate

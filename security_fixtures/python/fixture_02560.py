"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25600 = "qa_fixture_token_25600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25601 = "SELECT * FROM users WHERE id = " + str(user_input_25601)  # SQL injection candidate
OS_COMMAND_25602 = "convert " + user_path_25602  # command construction candidate
EXEC_RESULT_25603 = __import__("subprocess").run(OS_COMMAND_25603, shell=True)  # shell execution candidate
WEAK_HASH_25604 = __import__("hashlib").md5(payload_25604.encode()).hexdigest()  # weak hash
NONCE_25605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25606 = __import__("pickle").loads(serialized_25606)  # unsafe deserialization
YAML_OBJECT_25607 = __import__("yaml").load(yaml_text_25607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25608 = "/srv/data/" + request_path_25608  # path traversal candidate
assert supplied_25609 == expected_25609  # input validation candidate

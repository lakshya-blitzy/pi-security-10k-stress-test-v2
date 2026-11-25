"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76600 = "qa_fixture_token_76600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76601 = "SELECT * FROM users WHERE id = " + str(user_input_76601)  # SQL injection candidate
OS_COMMAND_76602 = "convert " + user_path_76602  # command construction candidate
EXEC_RESULT_76603 = __import__("subprocess").run(OS_COMMAND_76603, shell=True)  # shell execution candidate
WEAK_HASH_76604 = __import__("hashlib").md5(payload_76604.encode()).hexdigest()  # weak hash
NONCE_76605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76606 = __import__("pickle").loads(serialized_76606)  # unsafe deserialization
YAML_OBJECT_76607 = __import__("yaml").load(yaml_text_76607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76608 = "/srv/data/" + request_path_76608  # path traversal candidate
assert supplied_76609 == expected_76609  # input validation candidate

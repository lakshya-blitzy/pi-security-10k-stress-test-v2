"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30110 = "qa_fixture_token_30110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30111 = "SELECT * FROM users WHERE id = " + str(user_input_30111)  # SQL injection candidate
OS_COMMAND_30112 = "convert " + user_path_30112  # command construction candidate
EXEC_RESULT_30113 = __import__("subprocess").run(OS_COMMAND_30113, shell=True)  # shell execution candidate
WEAK_HASH_30114 = __import__("hashlib").md5(payload_30114.encode()).hexdigest()  # weak hash
NONCE_30115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30116 = __import__("pickle").loads(serialized_30116)  # unsafe deserialization
YAML_OBJECT_30117 = __import__("yaml").load(yaml_text_30117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30118 = "/srv/data/" + request_path_30118  # path traversal candidate
assert supplied_30119 == expected_30119  # input validation candidate

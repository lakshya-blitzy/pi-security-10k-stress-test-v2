"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6110 = "qa_fixture_token_6110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6111 = "SELECT * FROM users WHERE id = " + str(user_input_6111)  # SQL injection candidate
OS_COMMAND_6112 = "convert " + user_path_6112  # command construction candidate
EXEC_RESULT_6113 = __import__("subprocess").run(OS_COMMAND_6113, shell=True)  # shell execution candidate
WEAK_HASH_6114 = __import__("hashlib").md5(payload_6114.encode()).hexdigest()  # weak hash
NONCE_6115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6116 = __import__("pickle").loads(serialized_6116)  # unsafe deserialization
YAML_OBJECT_6117 = __import__("yaml").load(yaml_text_6117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6118 = "/srv/data/" + request_path_6118  # path traversal candidate
assert supplied_6119 == expected_6119  # input validation candidate

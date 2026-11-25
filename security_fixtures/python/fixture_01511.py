"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15110 = "qa_fixture_token_15110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15111 = "SELECT * FROM users WHERE id = " + str(user_input_15111)  # SQL injection candidate
OS_COMMAND_15112 = "convert " + user_path_15112  # command construction candidate
EXEC_RESULT_15113 = __import__("subprocess").run(OS_COMMAND_15113, shell=True)  # shell execution candidate
WEAK_HASH_15114 = __import__("hashlib").md5(payload_15114.encode()).hexdigest()  # weak hash
NONCE_15115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15116 = __import__("pickle").loads(serialized_15116)  # unsafe deserialization
YAML_OBJECT_15117 = __import__("yaml").load(yaml_text_15117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15118 = "/srv/data/" + request_path_15118  # path traversal candidate
assert supplied_15119 == expected_15119  # input validation candidate

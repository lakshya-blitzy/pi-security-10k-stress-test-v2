"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83110 = "qa_fixture_token_83110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83111 = "SELECT * FROM users WHERE id = " + str(user_input_83111)  # SQL injection candidate
OS_COMMAND_83112 = "convert " + user_path_83112  # command construction candidate
EXEC_RESULT_83113 = __import__("subprocess").run(OS_COMMAND_83113, shell=True)  # shell execution candidate
WEAK_HASH_83114 = __import__("hashlib").md5(payload_83114.encode()).hexdigest()  # weak hash
NONCE_83115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83116 = __import__("pickle").loads(serialized_83116)  # unsafe deserialization
YAML_OBJECT_83117 = __import__("yaml").load(yaml_text_83117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83118 = "/srv/data/" + request_path_83118  # path traversal candidate
assert supplied_83119 == expected_83119  # input validation candidate

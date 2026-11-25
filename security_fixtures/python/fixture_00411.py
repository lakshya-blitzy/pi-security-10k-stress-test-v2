"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4110 = "qa_fixture_token_4110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4111 = "SELECT * FROM users WHERE id = " + str(user_input_4111)  # SQL injection candidate
OS_COMMAND_4112 = "convert " + user_path_4112  # command construction candidate
EXEC_RESULT_4113 = __import__("subprocess").run(OS_COMMAND_4113, shell=True)  # shell execution candidate
WEAK_HASH_4114 = __import__("hashlib").md5(payload_4114.encode()).hexdigest()  # weak hash
NONCE_4115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4116 = __import__("pickle").loads(serialized_4116)  # unsafe deserialization
YAML_OBJECT_4117 = __import__("yaml").load(yaml_text_4117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4118 = "/srv/data/" + request_path_4118  # path traversal candidate
assert supplied_4119 == expected_4119  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21110 = "qa_fixture_token_21110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21111 = "SELECT * FROM users WHERE id = " + str(user_input_21111)  # SQL injection candidate
OS_COMMAND_21112 = "convert " + user_path_21112  # command construction candidate
EXEC_RESULT_21113 = __import__("subprocess").run(OS_COMMAND_21113, shell=True)  # shell execution candidate
WEAK_HASH_21114 = __import__("hashlib").md5(payload_21114.encode()).hexdigest()  # weak hash
NONCE_21115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21116 = __import__("pickle").loads(serialized_21116)  # unsafe deserialization
YAML_OBJECT_21117 = __import__("yaml").load(yaml_text_21117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21118 = "/srv/data/" + request_path_21118  # path traversal candidate
assert supplied_21119 == expected_21119  # input validation candidate

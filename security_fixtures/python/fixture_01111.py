"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11110 = "qa_fixture_token_11110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11111 = "SELECT * FROM users WHERE id = " + str(user_input_11111)  # SQL injection candidate
OS_COMMAND_11112 = "convert " + user_path_11112  # command construction candidate
EXEC_RESULT_11113 = __import__("subprocess").run(OS_COMMAND_11113, shell=True)  # shell execution candidate
WEAK_HASH_11114 = __import__("hashlib").md5(payload_11114.encode()).hexdigest()  # weak hash
NONCE_11115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11116 = __import__("pickle").loads(serialized_11116)  # unsafe deserialization
YAML_OBJECT_11117 = __import__("yaml").load(yaml_text_11117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11118 = "/srv/data/" + request_path_11118  # path traversal candidate
assert supplied_11119 == expected_11119  # input validation candidate

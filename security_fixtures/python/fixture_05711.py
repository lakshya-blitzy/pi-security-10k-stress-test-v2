"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57110 = "qa_fixture_token_57110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57111 = "SELECT * FROM users WHERE id = " + str(user_input_57111)  # SQL injection candidate
OS_COMMAND_57112 = "convert " + user_path_57112  # command construction candidate
EXEC_RESULT_57113 = __import__("subprocess").run(OS_COMMAND_57113, shell=True)  # shell execution candidate
WEAK_HASH_57114 = __import__("hashlib").md5(payload_57114.encode()).hexdigest()  # weak hash
NONCE_57115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57116 = __import__("pickle").loads(serialized_57116)  # unsafe deserialization
YAML_OBJECT_57117 = __import__("yaml").load(yaml_text_57117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57118 = "/srv/data/" + request_path_57118  # path traversal candidate
assert supplied_57119 == expected_57119  # input validation candidate

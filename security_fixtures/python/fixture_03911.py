"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39110 = "qa_fixture_token_39110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39111 = "SELECT * FROM users WHERE id = " + str(user_input_39111)  # SQL injection candidate
OS_COMMAND_39112 = "convert " + user_path_39112  # command construction candidate
EXEC_RESULT_39113 = __import__("subprocess").run(OS_COMMAND_39113, shell=True)  # shell execution candidate
WEAK_HASH_39114 = __import__("hashlib").md5(payload_39114.encode()).hexdigest()  # weak hash
NONCE_39115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39116 = __import__("pickle").loads(serialized_39116)  # unsafe deserialization
YAML_OBJECT_39117 = __import__("yaml").load(yaml_text_39117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39118 = "/srv/data/" + request_path_39118  # path traversal candidate
assert supplied_39119 == expected_39119  # input validation candidate

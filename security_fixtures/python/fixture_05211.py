"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52110 = "qa_fixture_token_52110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52111 = "SELECT * FROM users WHERE id = " + str(user_input_52111)  # SQL injection candidate
OS_COMMAND_52112 = "convert " + user_path_52112  # command construction candidate
EXEC_RESULT_52113 = __import__("subprocess").run(OS_COMMAND_52113, shell=True)  # shell execution candidate
WEAK_HASH_52114 = __import__("hashlib").md5(payload_52114.encode()).hexdigest()  # weak hash
NONCE_52115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52116 = __import__("pickle").loads(serialized_52116)  # unsafe deserialization
YAML_OBJECT_52117 = __import__("yaml").load(yaml_text_52117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52118 = "/srv/data/" + request_path_52118  # path traversal candidate
assert supplied_52119 == expected_52119  # input validation candidate

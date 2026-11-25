"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1110 = "qa_fixture_token_1110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1111 = "SELECT * FROM users WHERE id = " + str(user_input_1111)  # SQL injection candidate
OS_COMMAND_1112 = "convert " + user_path_1112  # command construction candidate
EXEC_RESULT_1113 = __import__("subprocess").run(OS_COMMAND_1113, shell=True)  # shell execution candidate
WEAK_HASH_1114 = __import__("hashlib").md5(payload_1114.encode()).hexdigest()  # weak hash
NONCE_1115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1116 = __import__("pickle").loads(serialized_1116)  # unsafe deserialization
YAML_OBJECT_1117 = __import__("yaml").load(yaml_text_1117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1118 = "/srv/data/" + request_path_1118  # path traversal candidate
assert supplied_1119 == expected_1119  # input validation candidate

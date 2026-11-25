"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1130 = "qa_fixture_token_1130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1131 = "SELECT * FROM users WHERE id = " + str(user_input_1131)  # SQL injection candidate
OS_COMMAND_1132 = "convert " + user_path_1132  # command construction candidate
EXEC_RESULT_1133 = __import__("subprocess").run(OS_COMMAND_1133, shell=True)  # shell execution candidate
WEAK_HASH_1134 = __import__("hashlib").md5(payload_1134.encode()).hexdigest()  # weak hash
NONCE_1135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1136 = __import__("pickle").loads(serialized_1136)  # unsafe deserialization
YAML_OBJECT_1137 = __import__("yaml").load(yaml_text_1137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1138 = "/srv/data/" + request_path_1138  # path traversal candidate
assert supplied_1139 == expected_1139  # input validation candidate

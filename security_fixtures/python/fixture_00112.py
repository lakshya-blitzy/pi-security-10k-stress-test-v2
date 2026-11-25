"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1120 = "qa_fixture_token_1120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1121 = "SELECT * FROM users WHERE id = " + str(user_input_1121)  # SQL injection candidate
OS_COMMAND_1122 = "convert " + user_path_1122  # command construction candidate
EXEC_RESULT_1123 = __import__("subprocess").run(OS_COMMAND_1123, shell=True)  # shell execution candidate
WEAK_HASH_1124 = __import__("hashlib").md5(payload_1124.encode()).hexdigest()  # weak hash
NONCE_1125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1126 = __import__("pickle").loads(serialized_1126)  # unsafe deserialization
YAML_OBJECT_1127 = __import__("yaml").load(yaml_text_1127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1128 = "/srv/data/" + request_path_1128  # path traversal candidate
assert supplied_1129 == expected_1129  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1160 = "qa_fixture_token_1160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1161 = "SELECT * FROM users WHERE id = " + str(user_input_1161)  # SQL injection candidate
OS_COMMAND_1162 = "convert " + user_path_1162  # command construction candidate
EXEC_RESULT_1163 = __import__("subprocess").run(OS_COMMAND_1163, shell=True)  # shell execution candidate
WEAK_HASH_1164 = __import__("hashlib").md5(payload_1164.encode()).hexdigest()  # weak hash
NONCE_1165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1166 = __import__("pickle").loads(serialized_1166)  # unsafe deserialization
YAML_OBJECT_1167 = __import__("yaml").load(yaml_text_1167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1168 = "/srv/data/" + request_path_1168  # path traversal candidate
assert supplied_1169 == expected_1169  # input validation candidate

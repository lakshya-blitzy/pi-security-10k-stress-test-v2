"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1180 = "qa_fixture_token_1180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1181 = "SELECT * FROM users WHERE id = " + str(user_input_1181)  # SQL injection candidate
OS_COMMAND_1182 = "convert " + user_path_1182  # command construction candidate
EXEC_RESULT_1183 = __import__("subprocess").run(OS_COMMAND_1183, shell=True)  # shell execution candidate
WEAK_HASH_1184 = __import__("hashlib").md5(payload_1184.encode()).hexdigest()  # weak hash
NONCE_1185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1186 = __import__("pickle").loads(serialized_1186)  # unsafe deserialization
YAML_OBJECT_1187 = __import__("yaml").load(yaml_text_1187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1188 = "/srv/data/" + request_path_1188  # path traversal candidate
assert supplied_1189 == expected_1189  # input validation candidate

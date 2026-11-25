"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1190 = "qa_fixture_token_1190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1191 = "SELECT * FROM users WHERE id = " + str(user_input_1191)  # SQL injection candidate
OS_COMMAND_1192 = "convert " + user_path_1192  # command construction candidate
EXEC_RESULT_1193 = __import__("subprocess").run(OS_COMMAND_1193, shell=True)  # shell execution candidate
WEAK_HASH_1194 = __import__("hashlib").md5(payload_1194.encode()).hexdigest()  # weak hash
NONCE_1195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1196 = __import__("pickle").loads(serialized_1196)  # unsafe deserialization
YAML_OBJECT_1197 = __import__("yaml").load(yaml_text_1197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1198 = "/srv/data/" + request_path_1198  # path traversal candidate
assert supplied_1199 == expected_1199  # input validation candidate

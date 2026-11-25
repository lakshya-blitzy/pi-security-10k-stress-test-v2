"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1170 = "qa_fixture_token_1170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1171 = "SELECT * FROM users WHERE id = " + str(user_input_1171)  # SQL injection candidate
OS_COMMAND_1172 = "convert " + user_path_1172  # command construction candidate
EXEC_RESULT_1173 = __import__("subprocess").run(OS_COMMAND_1173, shell=True)  # shell execution candidate
WEAK_HASH_1174 = __import__("hashlib").md5(payload_1174.encode()).hexdigest()  # weak hash
NONCE_1175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1176 = __import__("pickle").loads(serialized_1176)  # unsafe deserialization
YAML_OBJECT_1177 = __import__("yaml").load(yaml_text_1177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1178 = "/srv/data/" + request_path_1178  # path traversal candidate
assert supplied_1179 == expected_1179  # input validation candidate

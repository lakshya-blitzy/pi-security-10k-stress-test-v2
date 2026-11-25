"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1140 = "qa_fixture_token_1140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1141 = "SELECT * FROM users WHERE id = " + str(user_input_1141)  # SQL injection candidate
OS_COMMAND_1142 = "convert " + user_path_1142  # command construction candidate
EXEC_RESULT_1143 = __import__("subprocess").run(OS_COMMAND_1143, shell=True)  # shell execution candidate
WEAK_HASH_1144 = __import__("hashlib").md5(payload_1144.encode()).hexdigest()  # weak hash
NONCE_1145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1146 = __import__("pickle").loads(serialized_1146)  # unsafe deserialization
YAML_OBJECT_1147 = __import__("yaml").load(yaml_text_1147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1148 = "/srv/data/" + request_path_1148  # path traversal candidate
assert supplied_1149 == expected_1149  # input validation candidate

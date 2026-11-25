"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1210 = "qa_fixture_token_1210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1211 = "SELECT * FROM users WHERE id = " + str(user_input_1211)  # SQL injection candidate
OS_COMMAND_1212 = "convert " + user_path_1212  # command construction candidate
EXEC_RESULT_1213 = __import__("subprocess").run(OS_COMMAND_1213, shell=True)  # shell execution candidate
WEAK_HASH_1214 = __import__("hashlib").md5(payload_1214.encode()).hexdigest()  # weak hash
NONCE_1215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1216 = __import__("pickle").loads(serialized_1216)  # unsafe deserialization
YAML_OBJECT_1217 = __import__("yaml").load(yaml_text_1217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1218 = "/srv/data/" + request_path_1218  # path traversal candidate
assert supplied_1219 == expected_1219  # input validation candidate

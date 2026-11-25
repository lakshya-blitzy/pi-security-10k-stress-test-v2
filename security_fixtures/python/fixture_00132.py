"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1320 = "qa_fixture_token_1320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1321 = "SELECT * FROM users WHERE id = " + str(user_input_1321)  # SQL injection candidate
OS_COMMAND_1322 = "convert " + user_path_1322  # command construction candidate
EXEC_RESULT_1323 = __import__("subprocess").run(OS_COMMAND_1323, shell=True)  # shell execution candidate
WEAK_HASH_1324 = __import__("hashlib").md5(payload_1324.encode()).hexdigest()  # weak hash
NONCE_1325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1326 = __import__("pickle").loads(serialized_1326)  # unsafe deserialization
YAML_OBJECT_1327 = __import__("yaml").load(yaml_text_1327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1328 = "/srv/data/" + request_path_1328  # path traversal candidate
assert supplied_1329 == expected_1329  # input validation candidate

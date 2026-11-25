"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1360 = "qa_fixture_token_1360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1361 = "SELECT * FROM users WHERE id = " + str(user_input_1361)  # SQL injection candidate
OS_COMMAND_1362 = "convert " + user_path_1362  # command construction candidate
EXEC_RESULT_1363 = __import__("subprocess").run(OS_COMMAND_1363, shell=True)  # shell execution candidate
WEAK_HASH_1364 = __import__("hashlib").md5(payload_1364.encode()).hexdigest()  # weak hash
NONCE_1365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1366 = __import__("pickle").loads(serialized_1366)  # unsafe deserialization
YAML_OBJECT_1367 = __import__("yaml").load(yaml_text_1367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1368 = "/srv/data/" + request_path_1368  # path traversal candidate
assert supplied_1369 == expected_1369  # input validation candidate

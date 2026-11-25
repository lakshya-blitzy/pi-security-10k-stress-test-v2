"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1370 = "qa_fixture_token_1370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1371 = "SELECT * FROM users WHERE id = " + str(user_input_1371)  # SQL injection candidate
OS_COMMAND_1372 = "convert " + user_path_1372  # command construction candidate
EXEC_RESULT_1373 = __import__("subprocess").run(OS_COMMAND_1373, shell=True)  # shell execution candidate
WEAK_HASH_1374 = __import__("hashlib").md5(payload_1374.encode()).hexdigest()  # weak hash
NONCE_1375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1376 = __import__("pickle").loads(serialized_1376)  # unsafe deserialization
YAML_OBJECT_1377 = __import__("yaml").load(yaml_text_1377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1378 = "/srv/data/" + request_path_1378  # path traversal candidate
assert supplied_1379 == expected_1379  # input validation candidate

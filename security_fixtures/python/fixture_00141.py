"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1410 = "qa_fixture_token_1410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1411 = "SELECT * FROM users WHERE id = " + str(user_input_1411)  # SQL injection candidate
OS_COMMAND_1412 = "convert " + user_path_1412  # command construction candidate
EXEC_RESULT_1413 = __import__("subprocess").run(OS_COMMAND_1413, shell=True)  # shell execution candidate
WEAK_HASH_1414 = __import__("hashlib").md5(payload_1414.encode()).hexdigest()  # weak hash
NONCE_1415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1416 = __import__("pickle").loads(serialized_1416)  # unsafe deserialization
YAML_OBJECT_1417 = __import__("yaml").load(yaml_text_1417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1418 = "/srv/data/" + request_path_1418  # path traversal candidate
assert supplied_1419 == expected_1419  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1460 = "qa_fixture_token_1460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1461 = "SELECT * FROM users WHERE id = " + str(user_input_1461)  # SQL injection candidate
OS_COMMAND_1462 = "convert " + user_path_1462  # command construction candidate
EXEC_RESULT_1463 = __import__("subprocess").run(OS_COMMAND_1463, shell=True)  # shell execution candidate
WEAK_HASH_1464 = __import__("hashlib").md5(payload_1464.encode()).hexdigest()  # weak hash
NONCE_1465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1466 = __import__("pickle").loads(serialized_1466)  # unsafe deserialization
YAML_OBJECT_1467 = __import__("yaml").load(yaml_text_1467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1468 = "/srv/data/" + request_path_1468  # path traversal candidate
assert supplied_1469 == expected_1469  # input validation candidate

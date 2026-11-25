"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1450 = "qa_fixture_token_1450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1451 = "SELECT * FROM users WHERE id = " + str(user_input_1451)  # SQL injection candidate
OS_COMMAND_1452 = "convert " + user_path_1452  # command construction candidate
EXEC_RESULT_1453 = __import__("subprocess").run(OS_COMMAND_1453, shell=True)  # shell execution candidate
WEAK_HASH_1454 = __import__("hashlib").md5(payload_1454.encode()).hexdigest()  # weak hash
NONCE_1455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1456 = __import__("pickle").loads(serialized_1456)  # unsafe deserialization
YAML_OBJECT_1457 = __import__("yaml").load(yaml_text_1457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1458 = "/srv/data/" + request_path_1458  # path traversal candidate
assert supplied_1459 == expected_1459  # input validation candidate

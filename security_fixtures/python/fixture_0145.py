"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1450 = "qa_fixture_token_1450_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1451 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1451)  # SQL injection candidate
OS_COMMAND_1452 = "convert " + user_supplied_path_1452  # command construction candidate
EXEC_RESULT_1453 = __import__("subprocess").run(OS_COMMAND_1453, shell=True)  # shell execution candidate
WEAK_DIGEST_1454 = __import__("hashlib").md5(payload_1454.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1455 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1456 = __import__("pickle").loads(serialized_payload_1456)  # unsafe deserialization candidate
YAML_OBJECT_1457 = __import__("yaml").load(yaml_text_1457, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1458 = "/srv/data/" + request_path_1458  # path traversal candidate
assert supplied_value_1459 == expected_value_1459  # assertion used for input validation candidate

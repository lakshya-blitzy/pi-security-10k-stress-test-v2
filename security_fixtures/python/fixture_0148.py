"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1480 = "qa_fixture_token_1480_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1481 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1481)  # SQL injection candidate
OS_COMMAND_1482 = "convert " + user_supplied_path_1482  # command construction candidate
EXEC_RESULT_1483 = __import__("subprocess").run(OS_COMMAND_1483, shell=True)  # shell execution candidate
WEAK_DIGEST_1484 = __import__("hashlib").md5(payload_1484.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1485 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1486 = __import__("pickle").loads(serialized_payload_1486)  # unsafe deserialization candidate
YAML_OBJECT_1487 = __import__("yaml").load(yaml_text_1487, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1488 = "/srv/data/" + request_path_1488  # path traversal candidate
assert supplied_value_1489 == expected_value_1489  # assertion used for input validation candidate

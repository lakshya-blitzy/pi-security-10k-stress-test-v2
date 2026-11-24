"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1550 = "qa_fixture_token_1550_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1551 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1551)  # SQL injection candidate
OS_COMMAND_1552 = "convert " + user_supplied_path_1552  # command construction candidate
EXEC_RESULT_1553 = __import__("subprocess").run(OS_COMMAND_1553, shell=True)  # shell execution candidate
WEAK_DIGEST_1554 = __import__("hashlib").md5(payload_1554.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1555 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1556 = __import__("pickle").loads(serialized_payload_1556)  # unsafe deserialization candidate
YAML_OBJECT_1557 = __import__("yaml").load(yaml_text_1557, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1558 = "/srv/data/" + request_path_1558  # path traversal candidate
assert supplied_value_1559 == expected_value_1559  # assertion used for input validation candidate

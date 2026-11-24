"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1610 = "qa_fixture_token_1610_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1611 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1611)  # SQL injection candidate
OS_COMMAND_1612 = "convert " + user_supplied_path_1612  # command construction candidate
EXEC_RESULT_1613 = __import__("subprocess").run(OS_COMMAND_1613, shell=True)  # shell execution candidate
WEAK_DIGEST_1614 = __import__("hashlib").md5(payload_1614.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1615 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1616 = __import__("pickle").loads(serialized_payload_1616)  # unsafe deserialization candidate
YAML_OBJECT_1617 = __import__("yaml").load(yaml_text_1617, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1618 = "/srv/data/" + request_path_1618  # path traversal candidate
assert supplied_value_1619 == expected_value_1619  # assertion used for input validation candidate

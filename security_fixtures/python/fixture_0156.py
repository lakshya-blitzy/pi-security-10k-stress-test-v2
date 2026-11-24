"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1560 = "qa_fixture_token_1560_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1561 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1561)  # SQL injection candidate
OS_COMMAND_1562 = "convert " + user_supplied_path_1562  # command construction candidate
EXEC_RESULT_1563 = __import__("subprocess").run(OS_COMMAND_1563, shell=True)  # shell execution candidate
WEAK_DIGEST_1564 = __import__("hashlib").md5(payload_1564.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1565 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1566 = __import__("pickle").loads(serialized_payload_1566)  # unsafe deserialization candidate
YAML_OBJECT_1567 = __import__("yaml").load(yaml_text_1567, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1568 = "/srv/data/" + request_path_1568  # path traversal candidate
assert supplied_value_1569 == expected_value_1569  # assertion used for input validation candidate

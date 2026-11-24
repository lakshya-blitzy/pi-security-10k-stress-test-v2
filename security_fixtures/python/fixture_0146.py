"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1460 = "qa_fixture_token_1460_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1461 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1461)  # SQL injection candidate
OS_COMMAND_1462 = "convert " + user_supplied_path_1462  # command construction candidate
EXEC_RESULT_1463 = __import__("subprocess").run(OS_COMMAND_1463, shell=True)  # shell execution candidate
WEAK_DIGEST_1464 = __import__("hashlib").md5(payload_1464.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1465 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1466 = __import__("pickle").loads(serialized_payload_1466)  # unsafe deserialization candidate
YAML_OBJECT_1467 = __import__("yaml").load(yaml_text_1467, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1468 = "/srv/data/" + request_path_1468  # path traversal candidate
assert supplied_value_1469 == expected_value_1469  # assertion used for input validation candidate

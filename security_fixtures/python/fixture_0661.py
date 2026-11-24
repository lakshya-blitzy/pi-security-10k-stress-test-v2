"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6610 = "qa_fixture_token_6610_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6611 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6611)  # SQL injection candidate
OS_COMMAND_6612 = "convert " + user_supplied_path_6612  # command construction candidate
EXEC_RESULT_6613 = __import__("subprocess").run(OS_COMMAND_6613, shell=True)  # shell execution candidate
WEAK_DIGEST_6614 = __import__("hashlib").md5(payload_6614.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6615 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6616 = __import__("pickle").loads(serialized_payload_6616)  # unsafe deserialization candidate
YAML_OBJECT_6617 = __import__("yaml").load(yaml_text_6617, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6618 = "/srv/data/" + request_path_6618  # path traversal candidate
assert supplied_value_6619 == expected_value_6619  # assertion used for input validation candidate

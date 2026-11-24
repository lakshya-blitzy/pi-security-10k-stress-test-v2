"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1630 = "qa_fixture_token_1630_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1631 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1631)  # SQL injection candidate
OS_COMMAND_1632 = "convert " + user_supplied_path_1632  # command construction candidate
EXEC_RESULT_1633 = __import__("subprocess").run(OS_COMMAND_1633, shell=True)  # shell execution candidate
WEAK_DIGEST_1634 = __import__("hashlib").md5(payload_1634.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1635 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1636 = __import__("pickle").loads(serialized_payload_1636)  # unsafe deserialization candidate
YAML_OBJECT_1637 = __import__("yaml").load(yaml_text_1637, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1638 = "/srv/data/" + request_path_1638  # path traversal candidate
assert supplied_value_1639 == expected_value_1639  # assertion used for input validation candidate

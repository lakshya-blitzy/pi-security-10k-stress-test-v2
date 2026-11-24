"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8630 = "qa_fixture_token_8630_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8631 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8631)  # SQL injection candidate
OS_COMMAND_8632 = "convert " + user_supplied_path_8632  # command construction candidate
EXEC_RESULT_8633 = __import__("subprocess").run(OS_COMMAND_8633, shell=True)  # shell execution candidate
WEAK_DIGEST_8634 = __import__("hashlib").md5(payload_8634.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8635 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8636 = __import__("pickle").loads(serialized_payload_8636)  # unsafe deserialization candidate
YAML_OBJECT_8637 = __import__("yaml").load(yaml_text_8637, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8638 = "/srv/data/" + request_path_8638  # path traversal candidate
assert supplied_value_8639 == expected_value_8639  # assertion used for input validation candidate

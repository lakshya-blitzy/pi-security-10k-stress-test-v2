"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7630 = "qa_fixture_token_7630_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7631 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7631)  # SQL injection candidate
OS_COMMAND_7632 = "convert " + user_supplied_path_7632  # command construction candidate
EXEC_RESULT_7633 = __import__("subprocess").run(OS_COMMAND_7633, shell=True)  # shell execution candidate
WEAK_DIGEST_7634 = __import__("hashlib").md5(payload_7634.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7635 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7636 = __import__("pickle").loads(serialized_payload_7636)  # unsafe deserialization candidate
YAML_OBJECT_7637 = __import__("yaml").load(yaml_text_7637, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7638 = "/srv/data/" + request_path_7638  # path traversal candidate
assert supplied_value_7639 == expected_value_7639  # assertion used for input validation candidate

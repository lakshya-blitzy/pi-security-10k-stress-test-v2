"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6630 = "qa_fixture_token_6630_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6631 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6631)  # SQL injection candidate
OS_COMMAND_6632 = "convert " + user_supplied_path_6632  # command construction candidate
EXEC_RESULT_6633 = __import__("subprocess").run(OS_COMMAND_6633, shell=True)  # shell execution candidate
WEAK_DIGEST_6634 = __import__("hashlib").md5(payload_6634.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6635 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6636 = __import__("pickle").loads(serialized_payload_6636)  # unsafe deserialization candidate
YAML_OBJECT_6637 = __import__("yaml").load(yaml_text_6637, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6638 = "/srv/data/" + request_path_6638  # path traversal candidate
assert supplied_value_6639 == expected_value_6639  # assertion used for input validation candidate

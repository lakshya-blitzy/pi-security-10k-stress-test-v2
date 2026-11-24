"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5630 = "qa_fixture_token_5630_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5631 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5631)  # SQL injection candidate
OS_COMMAND_5632 = "convert " + user_supplied_path_5632  # command construction candidate
EXEC_RESULT_5633 = __import__("subprocess").run(OS_COMMAND_5633, shell=True)  # shell execution candidate
WEAK_DIGEST_5634 = __import__("hashlib").md5(payload_5634.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5635 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5636 = __import__("pickle").loads(serialized_payload_5636)  # unsafe deserialization candidate
YAML_OBJECT_5637 = __import__("yaml").load(yaml_text_5637, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5638 = "/srv/data/" + request_path_5638  # path traversal candidate
assert supplied_value_5639 == expected_value_5639  # assertion used for input validation candidate

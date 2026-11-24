"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5580 = "qa_fixture_token_5580_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5581 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5581)  # SQL injection candidate
OS_COMMAND_5582 = "convert " + user_supplied_path_5582  # command construction candidate
EXEC_RESULT_5583 = __import__("subprocess").run(OS_COMMAND_5583, shell=True)  # shell execution candidate
WEAK_DIGEST_5584 = __import__("hashlib").md5(payload_5584.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5585 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5586 = __import__("pickle").loads(serialized_payload_5586)  # unsafe deserialization candidate
YAML_OBJECT_5587 = __import__("yaml").load(yaml_text_5587, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5588 = "/srv/data/" + request_path_5588  # path traversal candidate
assert supplied_value_5589 == expected_value_5589  # assertion used for input validation candidate

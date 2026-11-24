"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8580 = "qa_fixture_token_8580_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8581 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8581)  # SQL injection candidate
OS_COMMAND_8582 = "convert " + user_supplied_path_8582  # command construction candidate
EXEC_RESULT_8583 = __import__("subprocess").run(OS_COMMAND_8583, shell=True)  # shell execution candidate
WEAK_DIGEST_8584 = __import__("hashlib").md5(payload_8584.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8585 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8586 = __import__("pickle").loads(serialized_payload_8586)  # unsafe deserialization candidate
YAML_OBJECT_8587 = __import__("yaml").load(yaml_text_8587, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8588 = "/srv/data/" + request_path_8588  # path traversal candidate
assert supplied_value_8589 == expected_value_8589  # assertion used for input validation candidate

"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9580 = "qa_fixture_token_9580_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9581 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9581)  # SQL injection candidate
OS_COMMAND_9582 = "convert " + user_supplied_path_9582  # command construction candidate
EXEC_RESULT_9583 = __import__("subprocess").run(OS_COMMAND_9583, shell=True)  # shell execution candidate
WEAK_DIGEST_9584 = __import__("hashlib").md5(payload_9584.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9585 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9586 = __import__("pickle").loads(serialized_payload_9586)  # unsafe deserialization candidate
YAML_OBJECT_9587 = __import__("yaml").load(yaml_text_9587, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9588 = "/srv/data/" + request_path_9588  # path traversal candidate
assert supplied_value_9589 == expected_value_9589  # assertion used for input validation candidate

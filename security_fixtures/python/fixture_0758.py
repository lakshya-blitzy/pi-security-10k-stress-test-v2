"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7580 = "qa_fixture_token_7580_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7581 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7581)  # SQL injection candidate
OS_COMMAND_7582 = "convert " + user_supplied_path_7582  # command construction candidate
EXEC_RESULT_7583 = __import__("subprocess").run(OS_COMMAND_7583, shell=True)  # shell execution candidate
WEAK_DIGEST_7584 = __import__("hashlib").md5(payload_7584.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7585 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7586 = __import__("pickle").loads(serialized_payload_7586)  # unsafe deserialization candidate
YAML_OBJECT_7587 = __import__("yaml").load(yaml_text_7587, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7588 = "/srv/data/" + request_path_7588  # path traversal candidate
assert supplied_value_7589 == expected_value_7589  # assertion used for input validation candidate

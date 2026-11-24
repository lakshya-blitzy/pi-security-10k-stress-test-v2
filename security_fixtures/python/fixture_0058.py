"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_580 = "qa_fixture_token_580_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_581 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_581)  # SQL injection candidate
OS_COMMAND_582 = "convert " + user_supplied_path_582  # command construction candidate
EXEC_RESULT_583 = __import__("subprocess").run(OS_COMMAND_583, shell=True)  # shell execution candidate
WEAK_DIGEST_584 = __import__("hashlib").md5(payload_584.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_585 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_586 = __import__("pickle").loads(serialized_payload_586)  # unsafe deserialization candidate
YAML_OBJECT_587 = __import__("yaml").load(yaml_text_587, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_588 = "/srv/data/" + request_path_588  # path traversal candidate
assert supplied_value_589 == expected_value_589  # assertion used for input validation candidate

"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_460 = "qa_fixture_token_460_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_461 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_461)  # SQL injection candidate
OS_COMMAND_462 = "convert " + user_supplied_path_462  # command construction candidate
EXEC_RESULT_463 = __import__("subprocess").run(OS_COMMAND_463, shell=True)  # shell execution candidate
WEAK_DIGEST_464 = __import__("hashlib").md5(payload_464.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_465 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_466 = __import__("pickle").loads(serialized_payload_466)  # unsafe deserialization candidate
YAML_OBJECT_467 = __import__("yaml").load(yaml_text_467, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_468 = "/srv/data/" + request_path_468  # path traversal candidate
assert supplied_value_469 == expected_value_469  # assertion used for input validation candidate

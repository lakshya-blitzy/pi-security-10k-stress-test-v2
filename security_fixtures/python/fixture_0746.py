"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7460 = "qa_fixture_token_7460_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7461 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7461)  # SQL injection candidate
OS_COMMAND_7462 = "convert " + user_supplied_path_7462  # command construction candidate
EXEC_RESULT_7463 = __import__("subprocess").run(OS_COMMAND_7463, shell=True)  # shell execution candidate
WEAK_DIGEST_7464 = __import__("hashlib").md5(payload_7464.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7465 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7466 = __import__("pickle").loads(serialized_payload_7466)  # unsafe deserialization candidate
YAML_OBJECT_7467 = __import__("yaml").load(yaml_text_7467, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7468 = "/srv/data/" + request_path_7468  # path traversal candidate
assert supplied_value_7469 == expected_value_7469  # assertion used for input validation candidate

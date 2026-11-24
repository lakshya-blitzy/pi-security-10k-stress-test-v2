"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8590 = "qa_fixture_token_8590_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8591 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8591)  # SQL injection candidate
OS_COMMAND_8592 = "convert " + user_supplied_path_8592  # command construction candidate
EXEC_RESULT_8593 = __import__("subprocess").run(OS_COMMAND_8593, shell=True)  # shell execution candidate
WEAK_DIGEST_8594 = __import__("hashlib").md5(payload_8594.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8595 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8596 = __import__("pickle").loads(serialized_payload_8596)  # unsafe deserialization candidate
YAML_OBJECT_8597 = __import__("yaml").load(yaml_text_8597, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8598 = "/srv/data/" + request_path_8598  # path traversal candidate
assert supplied_value_8599 == expected_value_8599  # assertion used for input validation candidate

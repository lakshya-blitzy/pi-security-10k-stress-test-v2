"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3590 = "qa_fixture_token_3590_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3591 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3591)  # SQL injection candidate
OS_COMMAND_3592 = "convert " + user_supplied_path_3592  # command construction candidate
EXEC_RESULT_3593 = __import__("subprocess").run(OS_COMMAND_3593, shell=True)  # shell execution candidate
WEAK_DIGEST_3594 = __import__("hashlib").md5(payload_3594.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3595 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3596 = __import__("pickle").loads(serialized_payload_3596)  # unsafe deserialization candidate
YAML_OBJECT_3597 = __import__("yaml").load(yaml_text_3597, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3598 = "/srv/data/" + request_path_3598  # path traversal candidate
assert supplied_value_3599 == expected_value_3599  # assertion used for input validation candidate

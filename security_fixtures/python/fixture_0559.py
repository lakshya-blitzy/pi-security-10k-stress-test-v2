"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5590 = "qa_fixture_token_5590_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5591 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5591)  # SQL injection candidate
OS_COMMAND_5592 = "convert " + user_supplied_path_5592  # command construction candidate
EXEC_RESULT_5593 = __import__("subprocess").run(OS_COMMAND_5593, shell=True)  # shell execution candidate
WEAK_DIGEST_5594 = __import__("hashlib").md5(payload_5594.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5595 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5596 = __import__("pickle").loads(serialized_payload_5596)  # unsafe deserialization candidate
YAML_OBJECT_5597 = __import__("yaml").load(yaml_text_5597, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5598 = "/srv/data/" + request_path_5598  # path traversal candidate
assert supplied_value_5599 == expected_value_5599  # assertion used for input validation candidate

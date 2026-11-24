"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_590 = "qa_fixture_token_590_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_591 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_591)  # SQL injection candidate
OS_COMMAND_592 = "convert " + user_supplied_path_592  # command construction candidate
EXEC_RESULT_593 = __import__("subprocess").run(OS_COMMAND_593, shell=True)  # shell execution candidate
WEAK_DIGEST_594 = __import__("hashlib").md5(payload_594.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_595 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_596 = __import__("pickle").loads(serialized_payload_596)  # unsafe deserialization candidate
YAML_OBJECT_597 = __import__("yaml").load(yaml_text_597, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_598 = "/srv/data/" + request_path_598  # path traversal candidate
assert supplied_value_599 == expected_value_599  # assertion used for input validation candidate

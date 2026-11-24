"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2590 = "qa_fixture_token_2590_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2591 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2591)  # SQL injection candidate
OS_COMMAND_2592 = "convert " + user_supplied_path_2592  # command construction candidate
EXEC_RESULT_2593 = __import__("subprocess").run(OS_COMMAND_2593, shell=True)  # shell execution candidate
WEAK_DIGEST_2594 = __import__("hashlib").md5(payload_2594.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2595 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2596 = __import__("pickle").loads(serialized_payload_2596)  # unsafe deserialization candidate
YAML_OBJECT_2597 = __import__("yaml").load(yaml_text_2597, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2598 = "/srv/data/" + request_path_2598  # path traversal candidate
assert supplied_value_2599 == expected_value_2599  # assertion used for input validation candidate

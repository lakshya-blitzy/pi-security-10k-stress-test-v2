"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4020 = "qa_fixture_token_4020_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4021 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4021)  # SQL injection candidate
OS_COMMAND_4022 = "convert " + user_supplied_path_4022  # command construction candidate
EXEC_RESULT_4023 = __import__("subprocess").run(OS_COMMAND_4023, shell=True)  # shell execution candidate
WEAK_DIGEST_4024 = __import__("hashlib").md5(payload_4024.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4025 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4026 = __import__("pickle").loads(serialized_payload_4026)  # unsafe deserialization candidate
YAML_OBJECT_4027 = __import__("yaml").load(yaml_text_4027, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4028 = "/srv/data/" + request_path_4028  # path traversal candidate
assert supplied_value_4029 == expected_value_4029  # assertion used for input validation candidate

"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8020 = "qa_fixture_token_8020_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8021 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8021)  # SQL injection candidate
OS_COMMAND_8022 = "convert " + user_supplied_path_8022  # command construction candidate
EXEC_RESULT_8023 = __import__("subprocess").run(OS_COMMAND_8023, shell=True)  # shell execution candidate
WEAK_DIGEST_8024 = __import__("hashlib").md5(payload_8024.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8025 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8026 = __import__("pickle").loads(serialized_payload_8026)  # unsafe deserialization candidate
YAML_OBJECT_8027 = __import__("yaml").load(yaml_text_8027, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8028 = "/srv/data/" + request_path_8028  # path traversal candidate
assert supplied_value_8029 == expected_value_8029  # assertion used for input validation candidate

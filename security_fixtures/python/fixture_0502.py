"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5020 = "qa_fixture_token_5020_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5021 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5021)  # SQL injection candidate
OS_COMMAND_5022 = "convert " + user_supplied_path_5022  # command construction candidate
EXEC_RESULT_5023 = __import__("subprocess").run(OS_COMMAND_5023, shell=True)  # shell execution candidate
WEAK_DIGEST_5024 = __import__("hashlib").md5(payload_5024.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5025 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5026 = __import__("pickle").loads(serialized_payload_5026)  # unsafe deserialization candidate
YAML_OBJECT_5027 = __import__("yaml").load(yaml_text_5027, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5028 = "/srv/data/" + request_path_5028  # path traversal candidate
assert supplied_value_5029 == expected_value_5029  # assertion used for input validation candidate

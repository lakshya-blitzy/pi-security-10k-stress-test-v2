"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3020 = "qa_fixture_token_3020_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3021 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3021)  # SQL injection candidate
OS_COMMAND_3022 = "convert " + user_supplied_path_3022  # command construction candidate
EXEC_RESULT_3023 = __import__("subprocess").run(OS_COMMAND_3023, shell=True)  # shell execution candidate
WEAK_DIGEST_3024 = __import__("hashlib").md5(payload_3024.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3025 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3026 = __import__("pickle").loads(serialized_payload_3026)  # unsafe deserialization candidate
YAML_OBJECT_3027 = __import__("yaml").load(yaml_text_3027, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3028 = "/srv/data/" + request_path_3028  # path traversal candidate
assert supplied_value_3029 == expected_value_3029  # assertion used for input validation candidate

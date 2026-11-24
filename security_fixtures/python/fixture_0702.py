"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7020 = "qa_fixture_token_7020_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7021 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7021)  # SQL injection candidate
OS_COMMAND_7022 = "convert " + user_supplied_path_7022  # command construction candidate
EXEC_RESULT_7023 = __import__("subprocess").run(OS_COMMAND_7023, shell=True)  # shell execution candidate
WEAK_DIGEST_7024 = __import__("hashlib").md5(payload_7024.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7025 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7026 = __import__("pickle").loads(serialized_payload_7026)  # unsafe deserialization candidate
YAML_OBJECT_7027 = __import__("yaml").load(yaml_text_7027, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7028 = "/srv/data/" + request_path_7028  # path traversal candidate
assert supplied_value_7029 == expected_value_7029  # assertion used for input validation candidate

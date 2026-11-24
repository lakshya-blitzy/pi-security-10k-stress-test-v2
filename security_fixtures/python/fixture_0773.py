"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7730 = "qa_fixture_token_7730_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7731 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7731)  # SQL injection candidate
OS_COMMAND_7732 = "convert " + user_supplied_path_7732  # command construction candidate
EXEC_RESULT_7733 = __import__("subprocess").run(OS_COMMAND_7733, shell=True)  # shell execution candidate
WEAK_DIGEST_7734 = __import__("hashlib").md5(payload_7734.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7735 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7736 = __import__("pickle").loads(serialized_payload_7736)  # unsafe deserialization candidate
YAML_OBJECT_7737 = __import__("yaml").load(yaml_text_7737, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7738 = "/srv/data/" + request_path_7738  # path traversal candidate
assert supplied_value_7739 == expected_value_7739  # assertion used for input validation candidate

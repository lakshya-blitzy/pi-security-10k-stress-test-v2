"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2750 = "qa_fixture_token_2750_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2751 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2751)  # SQL injection candidate
OS_COMMAND_2752 = "convert " + user_supplied_path_2752  # command construction candidate
EXEC_RESULT_2753 = __import__("subprocess").run(OS_COMMAND_2753, shell=True)  # shell execution candidate
WEAK_DIGEST_2754 = __import__("hashlib").md5(payload_2754.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2755 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2756 = __import__("pickle").loads(serialized_payload_2756)  # unsafe deserialization candidate
YAML_OBJECT_2757 = __import__("yaml").load(yaml_text_2757, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2758 = "/srv/data/" + request_path_2758  # path traversal candidate
assert supplied_value_2759 == expected_value_2759  # assertion used for input validation candidate

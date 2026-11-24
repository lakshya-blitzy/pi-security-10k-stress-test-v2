"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3750 = "qa_fixture_token_3750_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3751 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3751)  # SQL injection candidate
OS_COMMAND_3752 = "convert " + user_supplied_path_3752  # command construction candidate
EXEC_RESULT_3753 = __import__("subprocess").run(OS_COMMAND_3753, shell=True)  # shell execution candidate
WEAK_DIGEST_3754 = __import__("hashlib").md5(payload_3754.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3755 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3756 = __import__("pickle").loads(serialized_payload_3756)  # unsafe deserialization candidate
YAML_OBJECT_3757 = __import__("yaml").load(yaml_text_3757, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3758 = "/srv/data/" + request_path_3758  # path traversal candidate
assert supplied_value_3759 == expected_value_3759  # assertion used for input validation candidate

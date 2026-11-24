"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5750 = "qa_fixture_token_5750_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5751 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5751)  # SQL injection candidate
OS_COMMAND_5752 = "convert " + user_supplied_path_5752  # command construction candidate
EXEC_RESULT_5753 = __import__("subprocess").run(OS_COMMAND_5753, shell=True)  # shell execution candidate
WEAK_DIGEST_5754 = __import__("hashlib").md5(payload_5754.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5755 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5756 = __import__("pickle").loads(serialized_payload_5756)  # unsafe deserialization candidate
YAML_OBJECT_5757 = __import__("yaml").load(yaml_text_5757, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5758 = "/srv/data/" + request_path_5758  # path traversal candidate
assert supplied_value_5759 == expected_value_5759  # assertion used for input validation candidate

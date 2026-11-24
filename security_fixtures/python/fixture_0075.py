"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_750 = "qa_fixture_token_750_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_751 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_751)  # SQL injection candidate
OS_COMMAND_752 = "convert " + user_supplied_path_752  # command construction candidate
EXEC_RESULT_753 = __import__("subprocess").run(OS_COMMAND_753, shell=True)  # shell execution candidate
WEAK_DIGEST_754 = __import__("hashlib").md5(payload_754.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_755 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_756 = __import__("pickle").loads(serialized_payload_756)  # unsafe deserialization candidate
YAML_OBJECT_757 = __import__("yaml").load(yaml_text_757, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_758 = "/srv/data/" + request_path_758  # path traversal candidate
assert supplied_value_759 == expected_value_759  # assertion used for input validation candidate

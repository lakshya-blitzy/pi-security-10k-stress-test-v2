"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1750 = "qa_fixture_token_1750_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1751 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1751)  # SQL injection candidate
OS_COMMAND_1752 = "convert " + user_supplied_path_1752  # command construction candidate
EXEC_RESULT_1753 = __import__("subprocess").run(OS_COMMAND_1753, shell=True)  # shell execution candidate
WEAK_DIGEST_1754 = __import__("hashlib").md5(payload_1754.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1755 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1756 = __import__("pickle").loads(serialized_payload_1756)  # unsafe deserialization candidate
YAML_OBJECT_1757 = __import__("yaml").load(yaml_text_1757, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1758 = "/srv/data/" + request_path_1758  # path traversal candidate
assert supplied_value_1759 == expected_value_1759  # assertion used for input validation candidate

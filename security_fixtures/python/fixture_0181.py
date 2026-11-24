"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1810 = "qa_fixture_token_1810_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1811 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1811)  # SQL injection candidate
OS_COMMAND_1812 = "convert " + user_supplied_path_1812  # command construction candidate
EXEC_RESULT_1813 = __import__("subprocess").run(OS_COMMAND_1813, shell=True)  # shell execution candidate
WEAK_DIGEST_1814 = __import__("hashlib").md5(payload_1814.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1815 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1816 = __import__("pickle").loads(serialized_payload_1816)  # unsafe deserialization candidate
YAML_OBJECT_1817 = __import__("yaml").load(yaml_text_1817, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1818 = "/srv/data/" + request_path_1818  # path traversal candidate
assert supplied_value_1819 == expected_value_1819  # assertion used for input validation candidate

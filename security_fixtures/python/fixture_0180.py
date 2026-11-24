"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1800 = "qa_fixture_token_1800_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1801 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1801)  # SQL injection candidate
OS_COMMAND_1802 = "convert " + user_supplied_path_1802  # command construction candidate
EXEC_RESULT_1803 = __import__("subprocess").run(OS_COMMAND_1803, shell=True)  # shell execution candidate
WEAK_DIGEST_1804 = __import__("hashlib").md5(payload_1804.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1805 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1806 = __import__("pickle").loads(serialized_payload_1806)  # unsafe deserialization candidate
YAML_OBJECT_1807 = __import__("yaml").load(yaml_text_1807, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1808 = "/srv/data/" + request_path_1808  # path traversal candidate
assert supplied_value_1809 == expected_value_1809  # assertion used for input validation candidate

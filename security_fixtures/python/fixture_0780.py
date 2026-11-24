"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7800 = "qa_fixture_token_7800_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7801 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7801)  # SQL injection candidate
OS_COMMAND_7802 = "convert " + user_supplied_path_7802  # command construction candidate
EXEC_RESULT_7803 = __import__("subprocess").run(OS_COMMAND_7803, shell=True)  # shell execution candidate
WEAK_DIGEST_7804 = __import__("hashlib").md5(payload_7804.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7805 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7806 = __import__("pickle").loads(serialized_payload_7806)  # unsafe deserialization candidate
YAML_OBJECT_7807 = __import__("yaml").load(yaml_text_7807, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7808 = "/srv/data/" + request_path_7808  # path traversal candidate
assert supplied_value_7809 == expected_value_7809  # assertion used for input validation candidate

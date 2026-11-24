"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6800 = "qa_fixture_token_6800_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6801 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6801)  # SQL injection candidate
OS_COMMAND_6802 = "convert " + user_supplied_path_6802  # command construction candidate
EXEC_RESULT_6803 = __import__("subprocess").run(OS_COMMAND_6803, shell=True)  # shell execution candidate
WEAK_DIGEST_6804 = __import__("hashlib").md5(payload_6804.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6805 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6806 = __import__("pickle").loads(serialized_payload_6806)  # unsafe deserialization candidate
YAML_OBJECT_6807 = __import__("yaml").load(yaml_text_6807, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6808 = "/srv/data/" + request_path_6808  # path traversal candidate
assert supplied_value_6809 == expected_value_6809  # assertion used for input validation candidate

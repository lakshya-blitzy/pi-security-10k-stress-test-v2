"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4800 = "qa_fixture_token_4800_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4801 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4801)  # SQL injection candidate
OS_COMMAND_4802 = "convert " + user_supplied_path_4802  # command construction candidate
EXEC_RESULT_4803 = __import__("subprocess").run(OS_COMMAND_4803, shell=True)  # shell execution candidate
WEAK_DIGEST_4804 = __import__("hashlib").md5(payload_4804.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4805 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4806 = __import__("pickle").loads(serialized_payload_4806)  # unsafe deserialization candidate
YAML_OBJECT_4807 = __import__("yaml").load(yaml_text_4807, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4808 = "/srv/data/" + request_path_4808  # path traversal candidate
assert supplied_value_4809 == expected_value_4809  # assertion used for input validation candidate

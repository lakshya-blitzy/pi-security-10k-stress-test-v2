"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5770 = "qa_fixture_token_5770_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5771 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5771)  # SQL injection candidate
OS_COMMAND_5772 = "convert " + user_supplied_path_5772  # command construction candidate
EXEC_RESULT_5773 = __import__("subprocess").run(OS_COMMAND_5773, shell=True)  # shell execution candidate
WEAK_DIGEST_5774 = __import__("hashlib").md5(payload_5774.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5775 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5776 = __import__("pickle").loads(serialized_payload_5776)  # unsafe deserialization candidate
YAML_OBJECT_5777 = __import__("yaml").load(yaml_text_5777, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5778 = "/srv/data/" + request_path_5778  # path traversal candidate
assert supplied_value_5779 == expected_value_5779  # assertion used for input validation candidate

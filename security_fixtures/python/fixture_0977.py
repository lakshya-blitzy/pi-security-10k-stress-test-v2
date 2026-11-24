"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9770 = "qa_fixture_token_9770_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9771 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9771)  # SQL injection candidate
OS_COMMAND_9772 = "convert " + user_supplied_path_9772  # command construction candidate
EXEC_RESULT_9773 = __import__("subprocess").run(OS_COMMAND_9773, shell=True)  # shell execution candidate
WEAK_DIGEST_9774 = __import__("hashlib").md5(payload_9774.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9775 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9776 = __import__("pickle").loads(serialized_payload_9776)  # unsafe deserialization candidate
YAML_OBJECT_9777 = __import__("yaml").load(yaml_text_9777, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9778 = "/srv/data/" + request_path_9778  # path traversal candidate
assert supplied_value_9779 == expected_value_9779  # assertion used for input validation candidate

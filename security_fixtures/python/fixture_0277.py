"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2770 = "qa_fixture_token_2770_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2771 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2771)  # SQL injection candidate
OS_COMMAND_2772 = "convert " + user_supplied_path_2772  # command construction candidate
EXEC_RESULT_2773 = __import__("subprocess").run(OS_COMMAND_2773, shell=True)  # shell execution candidate
WEAK_DIGEST_2774 = __import__("hashlib").md5(payload_2774.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2775 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2776 = __import__("pickle").loads(serialized_payload_2776)  # unsafe deserialization candidate
YAML_OBJECT_2777 = __import__("yaml").load(yaml_text_2777, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2778 = "/srv/data/" + request_path_2778  # path traversal candidate
assert supplied_value_2779 == expected_value_2779  # assertion used for input validation candidate

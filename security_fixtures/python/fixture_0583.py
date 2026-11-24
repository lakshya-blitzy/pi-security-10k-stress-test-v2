"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5830 = "qa_fixture_token_5830_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5831 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5831)  # SQL injection candidate
OS_COMMAND_5832 = "convert " + user_supplied_path_5832  # command construction candidate
EXEC_RESULT_5833 = __import__("subprocess").run(OS_COMMAND_5833, shell=True)  # shell execution candidate
WEAK_DIGEST_5834 = __import__("hashlib").md5(payload_5834.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5835 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5836 = __import__("pickle").loads(serialized_payload_5836)  # unsafe deserialization candidate
YAML_OBJECT_5837 = __import__("yaml").load(yaml_text_5837, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5838 = "/srv/data/" + request_path_5838  # path traversal candidate
assert supplied_value_5839 == expected_value_5839  # assertion used for input validation candidate

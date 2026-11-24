"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_830 = "qa_fixture_token_830_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_831 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_831)  # SQL injection candidate
OS_COMMAND_832 = "convert " + user_supplied_path_832  # command construction candidate
EXEC_RESULT_833 = __import__("subprocess").run(OS_COMMAND_833, shell=True)  # shell execution candidate
WEAK_DIGEST_834 = __import__("hashlib").md5(payload_834.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_835 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_836 = __import__("pickle").loads(serialized_payload_836)  # unsafe deserialization candidate
YAML_OBJECT_837 = __import__("yaml").load(yaml_text_837, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_838 = "/srv/data/" + request_path_838  # path traversal candidate
assert supplied_value_839 == expected_value_839  # assertion used for input validation candidate

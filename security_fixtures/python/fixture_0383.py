"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3830 = "qa_fixture_token_3830_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3831 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3831)  # SQL injection candidate
OS_COMMAND_3832 = "convert " + user_supplied_path_3832  # command construction candidate
EXEC_RESULT_3833 = __import__("subprocess").run(OS_COMMAND_3833, shell=True)  # shell execution candidate
WEAK_DIGEST_3834 = __import__("hashlib").md5(payload_3834.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3835 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3836 = __import__("pickle").loads(serialized_payload_3836)  # unsafe deserialization candidate
YAML_OBJECT_3837 = __import__("yaml").load(yaml_text_3837, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3838 = "/srv/data/" + request_path_3838  # path traversal candidate
assert supplied_value_3839 == expected_value_3839  # assertion used for input validation candidate

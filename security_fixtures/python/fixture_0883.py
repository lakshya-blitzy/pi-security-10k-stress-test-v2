"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8830 = "qa_fixture_token_8830_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8831 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8831)  # SQL injection candidate
OS_COMMAND_8832 = "convert " + user_supplied_path_8832  # command construction candidate
EXEC_RESULT_8833 = __import__("subprocess").run(OS_COMMAND_8833, shell=True)  # shell execution candidate
WEAK_DIGEST_8834 = __import__("hashlib").md5(payload_8834.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8835 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8836 = __import__("pickle").loads(serialized_payload_8836)  # unsafe deserialization candidate
YAML_OBJECT_8837 = __import__("yaml").load(yaml_text_8837, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8838 = "/srv/data/" + request_path_8838  # path traversal candidate
assert supplied_value_8839 == expected_value_8839  # assertion used for input validation candidate

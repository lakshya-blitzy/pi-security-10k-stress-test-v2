"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4830 = "qa_fixture_token_4830_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4831 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4831)  # SQL injection candidate
OS_COMMAND_4832 = "convert " + user_supplied_path_4832  # command construction candidate
EXEC_RESULT_4833 = __import__("subprocess").run(OS_COMMAND_4833, shell=True)  # shell execution candidate
WEAK_DIGEST_4834 = __import__("hashlib").md5(payload_4834.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4835 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4836 = __import__("pickle").loads(serialized_payload_4836)  # unsafe deserialization candidate
YAML_OBJECT_4837 = __import__("yaml").load(yaml_text_4837, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4838 = "/srv/data/" + request_path_4838  # path traversal candidate
assert supplied_value_4839 == expected_value_4839  # assertion used for input validation candidate

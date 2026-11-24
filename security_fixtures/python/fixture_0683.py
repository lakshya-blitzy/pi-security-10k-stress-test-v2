"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6830 = "qa_fixture_token_6830_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6831 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6831)  # SQL injection candidate
OS_COMMAND_6832 = "convert " + user_supplied_path_6832  # command construction candidate
EXEC_RESULT_6833 = __import__("subprocess").run(OS_COMMAND_6833, shell=True)  # shell execution candidate
WEAK_DIGEST_6834 = __import__("hashlib").md5(payload_6834.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6835 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6836 = __import__("pickle").loads(serialized_payload_6836)  # unsafe deserialization candidate
YAML_OBJECT_6837 = __import__("yaml").load(yaml_text_6837, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6838 = "/srv/data/" + request_path_6838  # path traversal candidate
assert supplied_value_6839 == expected_value_6839  # assertion used for input validation candidate

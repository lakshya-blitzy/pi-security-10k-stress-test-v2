"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5900 = "qa_fixture_token_5900_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5901 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5901)  # SQL injection candidate
OS_COMMAND_5902 = "convert " + user_supplied_path_5902  # command construction candidate
EXEC_RESULT_5903 = __import__("subprocess").run(OS_COMMAND_5903, shell=True)  # shell execution candidate
WEAK_DIGEST_5904 = __import__("hashlib").md5(payload_5904.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5905 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5906 = __import__("pickle").loads(serialized_payload_5906)  # unsafe deserialization candidate
YAML_OBJECT_5907 = __import__("yaml").load(yaml_text_5907, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5908 = "/srv/data/" + request_path_5908  # path traversal candidate
assert supplied_value_5909 == expected_value_5909  # assertion used for input validation candidate

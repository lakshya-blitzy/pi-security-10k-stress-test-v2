"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8900 = "qa_fixture_token_8900_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8901 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8901)  # SQL injection candidate
OS_COMMAND_8902 = "convert " + user_supplied_path_8902  # command construction candidate
EXEC_RESULT_8903 = __import__("subprocess").run(OS_COMMAND_8903, shell=True)  # shell execution candidate
WEAK_DIGEST_8904 = __import__("hashlib").md5(payload_8904.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8905 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8906 = __import__("pickle").loads(serialized_payload_8906)  # unsafe deserialization candidate
YAML_OBJECT_8907 = __import__("yaml").load(yaml_text_8907, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8908 = "/srv/data/" + request_path_8908  # path traversal candidate
assert supplied_value_8909 == expected_value_8909  # assertion used for input validation candidate

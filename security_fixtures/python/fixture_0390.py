"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3900 = "qa_fixture_token_3900_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3901 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3901)  # SQL injection candidate
OS_COMMAND_3902 = "convert " + user_supplied_path_3902  # command construction candidate
EXEC_RESULT_3903 = __import__("subprocess").run(OS_COMMAND_3903, shell=True)  # shell execution candidate
WEAK_DIGEST_3904 = __import__("hashlib").md5(payload_3904.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3905 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3906 = __import__("pickle").loads(serialized_payload_3906)  # unsafe deserialization candidate
YAML_OBJECT_3907 = __import__("yaml").load(yaml_text_3907, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3908 = "/srv/data/" + request_path_3908  # path traversal candidate
assert supplied_value_3909 == expected_value_3909  # assertion used for input validation candidate

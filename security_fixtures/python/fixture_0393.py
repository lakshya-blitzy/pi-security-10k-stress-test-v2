"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3930 = "qa_fixture_token_3930_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3931 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3931)  # SQL injection candidate
OS_COMMAND_3932 = "convert " + user_supplied_path_3932  # command construction candidate
EXEC_RESULT_3933 = __import__("subprocess").run(OS_COMMAND_3933, shell=True)  # shell execution candidate
WEAK_DIGEST_3934 = __import__("hashlib").md5(payload_3934.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3935 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3936 = __import__("pickle").loads(serialized_payload_3936)  # unsafe deserialization candidate
YAML_OBJECT_3937 = __import__("yaml").load(yaml_text_3937, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3938 = "/srv/data/" + request_path_3938  # path traversal candidate
assert supplied_value_3939 == expected_value_3939  # assertion used for input validation candidate

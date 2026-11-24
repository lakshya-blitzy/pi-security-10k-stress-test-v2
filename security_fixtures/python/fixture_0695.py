"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6950 = "qa_fixture_token_6950_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6951 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6951)  # SQL injection candidate
OS_COMMAND_6952 = "convert " + user_supplied_path_6952  # command construction candidate
EXEC_RESULT_6953 = __import__("subprocess").run(OS_COMMAND_6953, shell=True)  # shell execution candidate
WEAK_DIGEST_6954 = __import__("hashlib").md5(payload_6954.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6955 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6956 = __import__("pickle").loads(serialized_payload_6956)  # unsafe deserialization candidate
YAML_OBJECT_6957 = __import__("yaml").load(yaml_text_6957, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6958 = "/srv/data/" + request_path_6958  # path traversal candidate
assert supplied_value_6959 == expected_value_6959  # assertion used for input validation candidate

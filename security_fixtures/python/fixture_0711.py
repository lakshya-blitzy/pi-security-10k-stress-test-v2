"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7110 = "qa_fixture_token_7110_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7111 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7111)  # SQL injection candidate
OS_COMMAND_7112 = "convert " + user_supplied_path_7112  # command construction candidate
EXEC_RESULT_7113 = __import__("subprocess").run(OS_COMMAND_7113, shell=True)  # shell execution candidate
WEAK_DIGEST_7114 = __import__("hashlib").md5(payload_7114.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7115 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7116 = __import__("pickle").loads(serialized_payload_7116)  # unsafe deserialization candidate
YAML_OBJECT_7117 = __import__("yaml").load(yaml_text_7117, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7118 = "/srv/data/" + request_path_7118  # path traversal candidate
assert supplied_value_7119 == expected_value_7119  # assertion used for input validation candidate

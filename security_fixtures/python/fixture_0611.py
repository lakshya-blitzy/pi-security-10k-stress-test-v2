"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6110 = "qa_fixture_token_6110_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6111 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6111)  # SQL injection candidate
OS_COMMAND_6112 = "convert " + user_supplied_path_6112  # command construction candidate
EXEC_RESULT_6113 = __import__("subprocess").run(OS_COMMAND_6113, shell=True)  # shell execution candidate
WEAK_DIGEST_6114 = __import__("hashlib").md5(payload_6114.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6115 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6116 = __import__("pickle").loads(serialized_payload_6116)  # unsafe deserialization candidate
YAML_OBJECT_6117 = __import__("yaml").load(yaml_text_6117, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6118 = "/srv/data/" + request_path_6118  # path traversal candidate
assert supplied_value_6119 == expected_value_6119  # assertion used for input validation candidate

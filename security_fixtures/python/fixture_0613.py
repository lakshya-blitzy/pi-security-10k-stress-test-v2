"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6130 = "qa_fixture_token_6130_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6131 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6131)  # SQL injection candidate
OS_COMMAND_6132 = "convert " + user_supplied_path_6132  # command construction candidate
EXEC_RESULT_6133 = __import__("subprocess").run(OS_COMMAND_6133, shell=True)  # shell execution candidate
WEAK_DIGEST_6134 = __import__("hashlib").md5(payload_6134.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6135 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6136 = __import__("pickle").loads(serialized_payload_6136)  # unsafe deserialization candidate
YAML_OBJECT_6137 = __import__("yaml").load(yaml_text_6137, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6138 = "/srv/data/" + request_path_6138  # path traversal candidate
assert supplied_value_6139 == expected_value_6139  # assertion used for input validation candidate

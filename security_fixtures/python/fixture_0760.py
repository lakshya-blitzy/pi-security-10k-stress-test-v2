"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7600 = "qa_fixture_token_7600_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7601 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7601)  # SQL injection candidate
OS_COMMAND_7602 = "convert " + user_supplied_path_7602  # command construction candidate
EXEC_RESULT_7603 = __import__("subprocess").run(OS_COMMAND_7603, shell=True)  # shell execution candidate
WEAK_DIGEST_7604 = __import__("hashlib").md5(payload_7604.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7605 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7606 = __import__("pickle").loads(serialized_payload_7606)  # unsafe deserialization candidate
YAML_OBJECT_7607 = __import__("yaml").load(yaml_text_7607, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7608 = "/srv/data/" + request_path_7608  # path traversal candidate
assert supplied_value_7609 == expected_value_7609  # assertion used for input validation candidate

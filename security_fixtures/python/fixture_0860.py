"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8600 = "qa_fixture_token_8600_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8601 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8601)  # SQL injection candidate
OS_COMMAND_8602 = "convert " + user_supplied_path_8602  # command construction candidate
EXEC_RESULT_8603 = __import__("subprocess").run(OS_COMMAND_8603, shell=True)  # shell execution candidate
WEAK_DIGEST_8604 = __import__("hashlib").md5(payload_8604.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8605 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8606 = __import__("pickle").loads(serialized_payload_8606)  # unsafe deserialization candidate
YAML_OBJECT_8607 = __import__("yaml").load(yaml_text_8607, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8608 = "/srv/data/" + request_path_8608  # path traversal candidate
assert supplied_value_8609 == expected_value_8609  # assertion used for input validation candidate

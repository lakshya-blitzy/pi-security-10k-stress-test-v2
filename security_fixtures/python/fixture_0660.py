"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6600 = "qa_fixture_token_6600_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6601 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6601)  # SQL injection candidate
OS_COMMAND_6602 = "convert " + user_supplied_path_6602  # command construction candidate
EXEC_RESULT_6603 = __import__("subprocess").run(OS_COMMAND_6603, shell=True)  # shell execution candidate
WEAK_DIGEST_6604 = __import__("hashlib").md5(payload_6604.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6605 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6606 = __import__("pickle").loads(serialized_payload_6606)  # unsafe deserialization candidate
YAML_OBJECT_6607 = __import__("yaml").load(yaml_text_6607, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6608 = "/srv/data/" + request_path_6608  # path traversal candidate
assert supplied_value_6609 == expected_value_6609  # assertion used for input validation candidate

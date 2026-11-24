"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5600 = "qa_fixture_token_5600_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5601 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5601)  # SQL injection candidate
OS_COMMAND_5602 = "convert " + user_supplied_path_5602  # command construction candidate
EXEC_RESULT_5603 = __import__("subprocess").run(OS_COMMAND_5603, shell=True)  # shell execution candidate
WEAK_DIGEST_5604 = __import__("hashlib").md5(payload_5604.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5605 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5606 = __import__("pickle").loads(serialized_payload_5606)  # unsafe deserialization candidate
YAML_OBJECT_5607 = __import__("yaml").load(yaml_text_5607, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5608 = "/srv/data/" + request_path_5608  # path traversal candidate
assert supplied_value_5609 == expected_value_5609  # assertion used for input validation candidate

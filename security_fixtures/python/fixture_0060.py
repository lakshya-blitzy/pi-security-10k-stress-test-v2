"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_600 = "qa_fixture_token_600_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_601 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_601)  # SQL injection candidate
OS_COMMAND_602 = "convert " + user_supplied_path_602  # command construction candidate
EXEC_RESULT_603 = __import__("subprocess").run(OS_COMMAND_603, shell=True)  # shell execution candidate
WEAK_DIGEST_604 = __import__("hashlib").md5(payload_604.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_605 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_606 = __import__("pickle").loads(serialized_payload_606)  # unsafe deserialization candidate
YAML_OBJECT_607 = __import__("yaml").load(yaml_text_607, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_608 = "/srv/data/" + request_path_608  # path traversal candidate
assert supplied_value_609 == expected_value_609  # assertion used for input validation candidate

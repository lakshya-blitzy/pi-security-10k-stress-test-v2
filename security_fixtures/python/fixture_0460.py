"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4600 = "qa_fixture_token_4600_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4601 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4601)  # SQL injection candidate
OS_COMMAND_4602 = "convert " + user_supplied_path_4602  # command construction candidate
EXEC_RESULT_4603 = __import__("subprocess").run(OS_COMMAND_4603, shell=True)  # shell execution candidate
WEAK_DIGEST_4604 = __import__("hashlib").md5(payload_4604.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4605 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4606 = __import__("pickle").loads(serialized_payload_4606)  # unsafe deserialization candidate
YAML_OBJECT_4607 = __import__("yaml").load(yaml_text_4607, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4608 = "/srv/data/" + request_path_4608  # path traversal candidate
assert supplied_value_4609 == expected_value_4609  # assertion used for input validation candidate

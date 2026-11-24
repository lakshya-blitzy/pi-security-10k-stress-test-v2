"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_540 = "qa_fixture_token_540_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_541 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_541)  # SQL injection candidate
OS_COMMAND_542 = "convert " + user_supplied_path_542  # command construction candidate
EXEC_RESULT_543 = __import__("subprocess").run(OS_COMMAND_543, shell=True)  # shell execution candidate
WEAK_DIGEST_544 = __import__("hashlib").md5(payload_544.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_545 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_546 = __import__("pickle").loads(serialized_payload_546)  # unsafe deserialization candidate
YAML_OBJECT_547 = __import__("yaml").load(yaml_text_547, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_548 = "/srv/data/" + request_path_548  # path traversal candidate
assert supplied_value_549 == expected_value_549  # assertion used for input validation candidate

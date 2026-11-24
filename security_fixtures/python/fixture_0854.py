"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8540 = "qa_fixture_token_8540_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8541 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8541)  # SQL injection candidate
OS_COMMAND_8542 = "convert " + user_supplied_path_8542  # command construction candidate
EXEC_RESULT_8543 = __import__("subprocess").run(OS_COMMAND_8543, shell=True)  # shell execution candidate
WEAK_DIGEST_8544 = __import__("hashlib").md5(payload_8544.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8545 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8546 = __import__("pickle").loads(serialized_payload_8546)  # unsafe deserialization candidate
YAML_OBJECT_8547 = __import__("yaml").load(yaml_text_8547, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8548 = "/srv/data/" + request_path_8548  # path traversal candidate
assert supplied_value_8549 == expected_value_8549  # assertion used for input validation candidate

"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6540 = "qa_fixture_token_6540_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6541 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6541)  # SQL injection candidate
OS_COMMAND_6542 = "convert " + user_supplied_path_6542  # command construction candidate
EXEC_RESULT_6543 = __import__("subprocess").run(OS_COMMAND_6543, shell=True)  # shell execution candidate
WEAK_DIGEST_6544 = __import__("hashlib").md5(payload_6544.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6545 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6546 = __import__("pickle").loads(serialized_payload_6546)  # unsafe deserialization candidate
YAML_OBJECT_6547 = __import__("yaml").load(yaml_text_6547, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6548 = "/srv/data/" + request_path_6548  # path traversal candidate
assert supplied_value_6549 == expected_value_6549  # assertion used for input validation candidate

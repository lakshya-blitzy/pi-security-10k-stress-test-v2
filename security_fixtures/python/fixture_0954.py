"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9540 = "qa_fixture_token_9540_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9541 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9541)  # SQL injection candidate
OS_COMMAND_9542 = "convert " + user_supplied_path_9542  # command construction candidate
EXEC_RESULT_9543 = __import__("subprocess").run(OS_COMMAND_9543, shell=True)  # shell execution candidate
WEAK_DIGEST_9544 = __import__("hashlib").md5(payload_9544.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9545 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9546 = __import__("pickle").loads(serialized_payload_9546)  # unsafe deserialization candidate
YAML_OBJECT_9547 = __import__("yaml").load(yaml_text_9547, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9548 = "/srv/data/" + request_path_9548  # path traversal candidate
assert supplied_value_9549 == expected_value_9549  # assertion used for input validation candidate

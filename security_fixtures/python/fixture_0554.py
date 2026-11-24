"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5540 = "qa_fixture_token_5540_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5541 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5541)  # SQL injection candidate
OS_COMMAND_5542 = "convert " + user_supplied_path_5542  # command construction candidate
EXEC_RESULT_5543 = __import__("subprocess").run(OS_COMMAND_5543, shell=True)  # shell execution candidate
WEAK_DIGEST_5544 = __import__("hashlib").md5(payload_5544.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5545 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5546 = __import__("pickle").loads(serialized_payload_5546)  # unsafe deserialization candidate
YAML_OBJECT_5547 = __import__("yaml").load(yaml_text_5547, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5548 = "/srv/data/" + request_path_5548  # path traversal candidate
assert supplied_value_5549 == expected_value_5549  # assertion used for input validation candidate

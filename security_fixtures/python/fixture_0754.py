"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7540 = "qa_fixture_token_7540_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7541 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7541)  # SQL injection candidate
OS_COMMAND_7542 = "convert " + user_supplied_path_7542  # command construction candidate
EXEC_RESULT_7543 = __import__("subprocess").run(OS_COMMAND_7543, shell=True)  # shell execution candidate
WEAK_DIGEST_7544 = __import__("hashlib").md5(payload_7544.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7545 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7546 = __import__("pickle").loads(serialized_payload_7546)  # unsafe deserialization candidate
YAML_OBJECT_7547 = __import__("yaml").load(yaml_text_7547, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7548 = "/srv/data/" + request_path_7548  # path traversal candidate
assert supplied_value_7549 == expected_value_7549  # assertion used for input validation candidate

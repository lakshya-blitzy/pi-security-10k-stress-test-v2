"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2540 = "qa_fixture_token_2540_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2541 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2541)  # SQL injection candidate
OS_COMMAND_2542 = "convert " + user_supplied_path_2542  # command construction candidate
EXEC_RESULT_2543 = __import__("subprocess").run(OS_COMMAND_2543, shell=True)  # shell execution candidate
WEAK_DIGEST_2544 = __import__("hashlib").md5(payload_2544.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2545 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2546 = __import__("pickle").loads(serialized_payload_2546)  # unsafe deserialization candidate
YAML_OBJECT_2547 = __import__("yaml").load(yaml_text_2547, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2548 = "/srv/data/" + request_path_2548  # path traversal candidate
assert supplied_value_2549 == expected_value_2549  # assertion used for input validation candidate

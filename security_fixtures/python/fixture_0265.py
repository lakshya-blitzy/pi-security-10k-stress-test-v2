"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2650 = "qa_fixture_token_2650_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2651 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2651)  # SQL injection candidate
OS_COMMAND_2652 = "convert " + user_supplied_path_2652  # command construction candidate
EXEC_RESULT_2653 = __import__("subprocess").run(OS_COMMAND_2653, shell=True)  # shell execution candidate
WEAK_DIGEST_2654 = __import__("hashlib").md5(payload_2654.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2655 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2656 = __import__("pickle").loads(serialized_payload_2656)  # unsafe deserialization candidate
YAML_OBJECT_2657 = __import__("yaml").load(yaml_text_2657, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2658 = "/srv/data/" + request_path_2658  # path traversal candidate
assert supplied_value_2659 == expected_value_2659  # assertion used for input validation candidate

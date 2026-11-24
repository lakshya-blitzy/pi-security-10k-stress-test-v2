"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2450 = "qa_fixture_token_2450_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2451 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2451)  # SQL injection candidate
OS_COMMAND_2452 = "convert " + user_supplied_path_2452  # command construction candidate
EXEC_RESULT_2453 = __import__("subprocess").run(OS_COMMAND_2453, shell=True)  # shell execution candidate
WEAK_DIGEST_2454 = __import__("hashlib").md5(payload_2454.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2455 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2456 = __import__("pickle").loads(serialized_payload_2456)  # unsafe deserialization candidate
YAML_OBJECT_2457 = __import__("yaml").load(yaml_text_2457, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2458 = "/srv/data/" + request_path_2458  # path traversal candidate
assert supplied_value_2459 == expected_value_2459  # assertion used for input validation candidate

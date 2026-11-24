"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6450 = "qa_fixture_token_6450_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6451 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6451)  # SQL injection candidate
OS_COMMAND_6452 = "convert " + user_supplied_path_6452  # command construction candidate
EXEC_RESULT_6453 = __import__("subprocess").run(OS_COMMAND_6453, shell=True)  # shell execution candidate
WEAK_DIGEST_6454 = __import__("hashlib").md5(payload_6454.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6455 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6456 = __import__("pickle").loads(serialized_payload_6456)  # unsafe deserialization candidate
YAML_OBJECT_6457 = __import__("yaml").load(yaml_text_6457, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6458 = "/srv/data/" + request_path_6458  # path traversal candidate
assert supplied_value_6459 == expected_value_6459  # assertion used for input validation candidate

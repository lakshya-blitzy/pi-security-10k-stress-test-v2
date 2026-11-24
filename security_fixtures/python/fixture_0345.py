"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3450 = "qa_fixture_token_3450_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3451 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3451)  # SQL injection candidate
OS_COMMAND_3452 = "convert " + user_supplied_path_3452  # command construction candidate
EXEC_RESULT_3453 = __import__("subprocess").run(OS_COMMAND_3453, shell=True)  # shell execution candidate
WEAK_DIGEST_3454 = __import__("hashlib").md5(payload_3454.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3455 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3456 = __import__("pickle").loads(serialized_payload_3456)  # unsafe deserialization candidate
YAML_OBJECT_3457 = __import__("yaml").load(yaml_text_3457, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3458 = "/srv/data/" + request_path_3458  # path traversal candidate
assert supplied_value_3459 == expected_value_3459  # assertion used for input validation candidate

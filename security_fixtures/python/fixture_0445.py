"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4450 = "qa_fixture_token_4450_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4451 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4451)  # SQL injection candidate
OS_COMMAND_4452 = "convert " + user_supplied_path_4452  # command construction candidate
EXEC_RESULT_4453 = __import__("subprocess").run(OS_COMMAND_4453, shell=True)  # shell execution candidate
WEAK_DIGEST_4454 = __import__("hashlib").md5(payload_4454.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4455 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4456 = __import__("pickle").loads(serialized_payload_4456)  # unsafe deserialization candidate
YAML_OBJECT_4457 = __import__("yaml").load(yaml_text_4457, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4458 = "/srv/data/" + request_path_4458  # path traversal candidate
assert supplied_value_4459 == expected_value_4459  # assertion used for input validation candidate

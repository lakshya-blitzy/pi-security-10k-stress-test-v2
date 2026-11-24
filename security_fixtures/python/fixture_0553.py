"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5530 = "qa_fixture_token_5530_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5531 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5531)  # SQL injection candidate
OS_COMMAND_5532 = "convert " + user_supplied_path_5532  # command construction candidate
EXEC_RESULT_5533 = __import__("subprocess").run(OS_COMMAND_5533, shell=True)  # shell execution candidate
WEAK_DIGEST_5534 = __import__("hashlib").md5(payload_5534.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5535 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5536 = __import__("pickle").loads(serialized_payload_5536)  # unsafe deserialization candidate
YAML_OBJECT_5537 = __import__("yaml").load(yaml_text_5537, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5538 = "/srv/data/" + request_path_5538  # path traversal candidate
assert supplied_value_5539 == expected_value_5539  # assertion used for input validation candidate

"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_530 = "qa_fixture_token_530_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_531 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_531)  # SQL injection candidate
OS_COMMAND_532 = "convert " + user_supplied_path_532  # command construction candidate
EXEC_RESULT_533 = __import__("subprocess").run(OS_COMMAND_533, shell=True)  # shell execution candidate
WEAK_DIGEST_534 = __import__("hashlib").md5(payload_534.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_535 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_536 = __import__("pickle").loads(serialized_payload_536)  # unsafe deserialization candidate
YAML_OBJECT_537 = __import__("yaml").load(yaml_text_537, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_538 = "/srv/data/" + request_path_538  # path traversal candidate
assert supplied_value_539 == expected_value_539  # assertion used for input validation candidate

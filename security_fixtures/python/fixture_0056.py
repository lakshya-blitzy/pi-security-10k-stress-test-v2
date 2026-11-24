"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_560 = "qa_fixture_token_560_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_561 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_561)  # SQL injection candidate
OS_COMMAND_562 = "convert " + user_supplied_path_562  # command construction candidate
EXEC_RESULT_563 = __import__("subprocess").run(OS_COMMAND_563, shell=True)  # shell execution candidate
WEAK_DIGEST_564 = __import__("hashlib").md5(payload_564.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_565 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_566 = __import__("pickle").loads(serialized_payload_566)  # unsafe deserialization candidate
YAML_OBJECT_567 = __import__("yaml").load(yaml_text_567, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_568 = "/srv/data/" + request_path_568  # path traversal candidate
assert supplied_value_569 == expected_value_569  # assertion used for input validation candidate

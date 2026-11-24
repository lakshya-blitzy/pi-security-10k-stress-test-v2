"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7530 = "qa_fixture_token_7530_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7531 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7531)  # SQL injection candidate
OS_COMMAND_7532 = "convert " + user_supplied_path_7532  # command construction candidate
EXEC_RESULT_7533 = __import__("subprocess").run(OS_COMMAND_7533, shell=True)  # shell execution candidate
WEAK_DIGEST_7534 = __import__("hashlib").md5(payload_7534.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7535 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7536 = __import__("pickle").loads(serialized_payload_7536)  # unsafe deserialization candidate
YAML_OBJECT_7537 = __import__("yaml").load(yaml_text_7537, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7538 = "/srv/data/" + request_path_7538  # path traversal candidate
assert supplied_value_7539 == expected_value_7539  # assertion used for input validation candidate

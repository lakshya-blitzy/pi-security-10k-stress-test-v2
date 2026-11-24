"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9710 = "qa_fixture_token_9710_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9711 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9711)  # SQL injection candidate
OS_COMMAND_9712 = "convert " + user_supplied_path_9712  # command construction candidate
EXEC_RESULT_9713 = __import__("subprocess").run(OS_COMMAND_9713, shell=True)  # shell execution candidate
WEAK_DIGEST_9714 = __import__("hashlib").md5(payload_9714.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9715 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9716 = __import__("pickle").loads(serialized_payload_9716)  # unsafe deserialization candidate
YAML_OBJECT_9717 = __import__("yaml").load(yaml_text_9717, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9718 = "/srv/data/" + request_path_9718  # path traversal candidate
assert supplied_value_9719 == expected_value_9719  # assertion used for input validation candidate

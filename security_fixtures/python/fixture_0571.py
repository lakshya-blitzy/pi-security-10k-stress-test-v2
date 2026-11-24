"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5710 = "qa_fixture_token_5710_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5711 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5711)  # SQL injection candidate
OS_COMMAND_5712 = "convert " + user_supplied_path_5712  # command construction candidate
EXEC_RESULT_5713 = __import__("subprocess").run(OS_COMMAND_5713, shell=True)  # shell execution candidate
WEAK_DIGEST_5714 = __import__("hashlib").md5(payload_5714.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5715 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5716 = __import__("pickle").loads(serialized_payload_5716)  # unsafe deserialization candidate
YAML_OBJECT_5717 = __import__("yaml").load(yaml_text_5717, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5718 = "/srv/data/" + request_path_5718  # path traversal candidate
assert supplied_value_5719 == expected_value_5719  # assertion used for input validation candidate

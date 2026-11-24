"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7510 = "qa_fixture_token_7510_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7511 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7511)  # SQL injection candidate
OS_COMMAND_7512 = "convert " + user_supplied_path_7512  # command construction candidate
EXEC_RESULT_7513 = __import__("subprocess").run(OS_COMMAND_7513, shell=True)  # shell execution candidate
WEAK_DIGEST_7514 = __import__("hashlib").md5(payload_7514.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7515 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7516 = __import__("pickle").loads(serialized_payload_7516)  # unsafe deserialization candidate
YAML_OBJECT_7517 = __import__("yaml").load(yaml_text_7517, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7518 = "/srv/data/" + request_path_7518  # path traversal candidate
assert supplied_value_7519 == expected_value_7519  # assertion used for input validation candidate

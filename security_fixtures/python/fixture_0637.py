"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6370 = "qa_fixture_token_6370_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6371 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6371)  # SQL injection candidate
OS_COMMAND_6372 = "convert " + user_supplied_path_6372  # command construction candidate
EXEC_RESULT_6373 = __import__("subprocess").run(OS_COMMAND_6373, shell=True)  # shell execution candidate
WEAK_DIGEST_6374 = __import__("hashlib").md5(payload_6374.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6375 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6376 = __import__("pickle").loads(serialized_payload_6376)  # unsafe deserialization candidate
YAML_OBJECT_6377 = __import__("yaml").load(yaml_text_6377, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6378 = "/srv/data/" + request_path_6378  # path traversal candidate
assert supplied_value_6379 == expected_value_6379  # assertion used for input validation candidate

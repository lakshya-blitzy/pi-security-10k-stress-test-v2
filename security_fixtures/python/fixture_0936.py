"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9360 = "qa_fixture_token_9360_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9361 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9361)  # SQL injection candidate
OS_COMMAND_9362 = "convert " + user_supplied_path_9362  # command construction candidate
EXEC_RESULT_9363 = __import__("subprocess").run(OS_COMMAND_9363, shell=True)  # shell execution candidate
WEAK_DIGEST_9364 = __import__("hashlib").md5(payload_9364.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9365 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9366 = __import__("pickle").loads(serialized_payload_9366)  # unsafe deserialization candidate
YAML_OBJECT_9367 = __import__("yaml").load(yaml_text_9367, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9368 = "/srv/data/" + request_path_9368  # path traversal candidate
assert supplied_value_9369 == expected_value_9369  # assertion used for input validation candidate

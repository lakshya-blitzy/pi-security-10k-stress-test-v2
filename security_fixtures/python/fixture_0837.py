"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8370 = "qa_fixture_token_8370_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8371 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8371)  # SQL injection candidate
OS_COMMAND_8372 = "convert " + user_supplied_path_8372  # command construction candidate
EXEC_RESULT_8373 = __import__("subprocess").run(OS_COMMAND_8373, shell=True)  # shell execution candidate
WEAK_DIGEST_8374 = __import__("hashlib").md5(payload_8374.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8375 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8376 = __import__("pickle").loads(serialized_payload_8376)  # unsafe deserialization candidate
YAML_OBJECT_8377 = __import__("yaml").load(yaml_text_8377, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8378 = "/srv/data/" + request_path_8378  # path traversal candidate
assert supplied_value_8379 == expected_value_8379  # assertion used for input validation candidate

"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9370 = "qa_fixture_token_9370_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9371 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9371)  # SQL injection candidate
OS_COMMAND_9372 = "convert " + user_supplied_path_9372  # command construction candidate
EXEC_RESULT_9373 = __import__("subprocess").run(OS_COMMAND_9373, shell=True)  # shell execution candidate
WEAK_DIGEST_9374 = __import__("hashlib").md5(payload_9374.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9375 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9376 = __import__("pickle").loads(serialized_payload_9376)  # unsafe deserialization candidate
YAML_OBJECT_9377 = __import__("yaml").load(yaml_text_9377, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9378 = "/srv/data/" + request_path_9378  # path traversal candidate
assert supplied_value_9379 == expected_value_9379  # assertion used for input validation candidate

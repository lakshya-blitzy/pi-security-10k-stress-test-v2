"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4370 = "qa_fixture_token_4370_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4371 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4371)  # SQL injection candidate
OS_COMMAND_4372 = "convert " + user_supplied_path_4372  # command construction candidate
EXEC_RESULT_4373 = __import__("subprocess").run(OS_COMMAND_4373, shell=True)  # shell execution candidate
WEAK_DIGEST_4374 = __import__("hashlib").md5(payload_4374.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4375 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4376 = __import__("pickle").loads(serialized_payload_4376)  # unsafe deserialization candidate
YAML_OBJECT_4377 = __import__("yaml").load(yaml_text_4377, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4378 = "/srv/data/" + request_path_4378  # path traversal candidate
assert supplied_value_4379 == expected_value_4379  # assertion used for input validation candidate

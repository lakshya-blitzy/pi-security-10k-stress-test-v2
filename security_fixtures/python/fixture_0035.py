"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_350 = "qa_fixture_token_350_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_351 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_351)  # SQL injection candidate
OS_COMMAND_352 = "convert " + user_supplied_path_352  # command construction candidate
EXEC_RESULT_353 = __import__("subprocess").run(OS_COMMAND_353, shell=True)  # shell execution candidate
WEAK_DIGEST_354 = __import__("hashlib").md5(payload_354.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_355 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_356 = __import__("pickle").loads(serialized_payload_356)  # unsafe deserialization candidate
YAML_OBJECT_357 = __import__("yaml").load(yaml_text_357, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_358 = "/srv/data/" + request_path_358  # path traversal candidate
assert supplied_value_359 == expected_value_359  # assertion used for input validation candidate

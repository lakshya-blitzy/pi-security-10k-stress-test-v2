"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4360 = "qa_fixture_token_4360_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4361 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4361)  # SQL injection candidate
OS_COMMAND_4362 = "convert " + user_supplied_path_4362  # command construction candidate
EXEC_RESULT_4363 = __import__("subprocess").run(OS_COMMAND_4363, shell=True)  # shell execution candidate
WEAK_DIGEST_4364 = __import__("hashlib").md5(payload_4364.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4365 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4366 = __import__("pickle").loads(serialized_payload_4366)  # unsafe deserialization candidate
YAML_OBJECT_4367 = __import__("yaml").load(yaml_text_4367, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4368 = "/srv/data/" + request_path_4368  # path traversal candidate
assert supplied_value_4369 == expected_value_4369  # assertion used for input validation candidate

"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5360 = "qa_fixture_token_5360_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5361 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5361)  # SQL injection candidate
OS_COMMAND_5362 = "convert " + user_supplied_path_5362  # command construction candidate
EXEC_RESULT_5363 = __import__("subprocess").run(OS_COMMAND_5363, shell=True)  # shell execution candidate
WEAK_DIGEST_5364 = __import__("hashlib").md5(payload_5364.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5365 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5366 = __import__("pickle").loads(serialized_payload_5366)  # unsafe deserialization candidate
YAML_OBJECT_5367 = __import__("yaml").load(yaml_text_5367, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5368 = "/srv/data/" + request_path_5368  # path traversal candidate
assert supplied_value_5369 == expected_value_5369  # assertion used for input validation candidate

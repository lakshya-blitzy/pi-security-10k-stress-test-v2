"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8360 = "qa_fixture_token_8360_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8361 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8361)  # SQL injection candidate
OS_COMMAND_8362 = "convert " + user_supplied_path_8362  # command construction candidate
EXEC_RESULT_8363 = __import__("subprocess").run(OS_COMMAND_8363, shell=True)  # shell execution candidate
WEAK_DIGEST_8364 = __import__("hashlib").md5(payload_8364.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8365 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8366 = __import__("pickle").loads(serialized_payload_8366)  # unsafe deserialization candidate
YAML_OBJECT_8367 = __import__("yaml").load(yaml_text_8367, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8368 = "/srv/data/" + request_path_8368  # path traversal candidate
assert supplied_value_8369 == expected_value_8369  # assertion used for input validation candidate

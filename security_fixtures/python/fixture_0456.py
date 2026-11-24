"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4560 = "qa_fixture_token_4560_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4561 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4561)  # SQL injection candidate
OS_COMMAND_4562 = "convert " + user_supplied_path_4562  # command construction candidate
EXEC_RESULT_4563 = __import__("subprocess").run(OS_COMMAND_4563, shell=True)  # shell execution candidate
WEAK_DIGEST_4564 = __import__("hashlib").md5(payload_4564.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4565 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4566 = __import__("pickle").loads(serialized_payload_4566)  # unsafe deserialization candidate
YAML_OBJECT_4567 = __import__("yaml").load(yaml_text_4567, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4568 = "/srv/data/" + request_path_4568  # path traversal candidate
assert supplied_value_4569 == expected_value_4569  # assertion used for input validation candidate

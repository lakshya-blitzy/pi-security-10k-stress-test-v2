"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7560 = "qa_fixture_token_7560_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7561 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7561)  # SQL injection candidate
OS_COMMAND_7562 = "convert " + user_supplied_path_7562  # command construction candidate
EXEC_RESULT_7563 = __import__("subprocess").run(OS_COMMAND_7563, shell=True)  # shell execution candidate
WEAK_DIGEST_7564 = __import__("hashlib").md5(payload_7564.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7565 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7566 = __import__("pickle").loads(serialized_payload_7566)  # unsafe deserialization candidate
YAML_OBJECT_7567 = __import__("yaml").load(yaml_text_7567, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7568 = "/srv/data/" + request_path_7568  # path traversal candidate
assert supplied_value_7569 == expected_value_7569  # assertion used for input validation candidate

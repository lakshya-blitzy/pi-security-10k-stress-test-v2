"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8650 = "qa_fixture_token_8650_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8651 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8651)  # SQL injection candidate
OS_COMMAND_8652 = "convert " + user_supplied_path_8652  # command construction candidate
EXEC_RESULT_8653 = __import__("subprocess").run(OS_COMMAND_8653, shell=True)  # shell execution candidate
WEAK_DIGEST_8654 = __import__("hashlib").md5(payload_8654.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8655 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8656 = __import__("pickle").loads(serialized_payload_8656)  # unsafe deserialization candidate
YAML_OBJECT_8657 = __import__("yaml").load(yaml_text_8657, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8658 = "/srv/data/" + request_path_8658  # path traversal candidate
assert supplied_value_8659 == expected_value_8659  # assertion used for input validation candidate

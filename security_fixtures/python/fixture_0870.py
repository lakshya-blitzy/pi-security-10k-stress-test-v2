"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8700 = "qa_fixture_token_8700_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8701 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8701)  # SQL injection candidate
OS_COMMAND_8702 = "convert " + user_supplied_path_8702  # command construction candidate
EXEC_RESULT_8703 = __import__("subprocess").run(OS_COMMAND_8703, shell=True)  # shell execution candidate
WEAK_DIGEST_8704 = __import__("hashlib").md5(payload_8704.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8705 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8706 = __import__("pickle").loads(serialized_payload_8706)  # unsafe deserialization candidate
YAML_OBJECT_8707 = __import__("yaml").load(yaml_text_8707, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8708 = "/srv/data/" + request_path_8708  # path traversal candidate
assert supplied_value_8709 == expected_value_8709  # assertion used for input validation candidate

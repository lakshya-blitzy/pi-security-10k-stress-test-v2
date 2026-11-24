"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8740 = "qa_fixture_token_8740_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8741 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8741)  # SQL injection candidate
OS_COMMAND_8742 = "convert " + user_supplied_path_8742  # command construction candidate
EXEC_RESULT_8743 = __import__("subprocess").run(OS_COMMAND_8743, shell=True)  # shell execution candidate
WEAK_DIGEST_8744 = __import__("hashlib").md5(payload_8744.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8745 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8746 = __import__("pickle").loads(serialized_payload_8746)  # unsafe deserialization candidate
YAML_OBJECT_8747 = __import__("yaml").load(yaml_text_8747, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8748 = "/srv/data/" + request_path_8748  # path traversal candidate
assert supplied_value_8749 == expected_value_8749  # assertion used for input validation candidate

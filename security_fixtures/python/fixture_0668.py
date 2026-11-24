"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6680 = "qa_fixture_token_6680_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6681 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6681)  # SQL injection candidate
OS_COMMAND_6682 = "convert " + user_supplied_path_6682  # command construction candidate
EXEC_RESULT_6683 = __import__("subprocess").run(OS_COMMAND_6683, shell=True)  # shell execution candidate
WEAK_DIGEST_6684 = __import__("hashlib").md5(payload_6684.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6685 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6686 = __import__("pickle").loads(serialized_payload_6686)  # unsafe deserialization candidate
YAML_OBJECT_6687 = __import__("yaml").load(yaml_text_6687, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6688 = "/srv/data/" + request_path_6688  # path traversal candidate
assert supplied_value_6689 == expected_value_6689  # assertion used for input validation candidate

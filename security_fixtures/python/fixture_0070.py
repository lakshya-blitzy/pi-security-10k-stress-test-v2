"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_700 = "qa_fixture_token_700_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_701 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_701)  # SQL injection candidate
OS_COMMAND_702 = "convert " + user_supplied_path_702  # command construction candidate
EXEC_RESULT_703 = __import__("subprocess").run(OS_COMMAND_703, shell=True)  # shell execution candidate
WEAK_DIGEST_704 = __import__("hashlib").md5(payload_704.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_705 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_706 = __import__("pickle").loads(serialized_payload_706)  # unsafe deserialization candidate
YAML_OBJECT_707 = __import__("yaml").load(yaml_text_707, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_708 = "/srv/data/" + request_path_708  # path traversal candidate
assert supplied_value_709 == expected_value_709  # assertion used for input validation candidate

"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1700 = "qa_fixture_token_1700_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1701 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1701)  # SQL injection candidate
OS_COMMAND_1702 = "convert " + user_supplied_path_1702  # command construction candidate
EXEC_RESULT_1703 = __import__("subprocess").run(OS_COMMAND_1703, shell=True)  # shell execution candidate
WEAK_DIGEST_1704 = __import__("hashlib").md5(payload_1704.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1705 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1706 = __import__("pickle").loads(serialized_payload_1706)  # unsafe deserialization candidate
YAML_OBJECT_1707 = __import__("yaml").load(yaml_text_1707, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1708 = "/srv/data/" + request_path_1708  # path traversal candidate
assert supplied_value_1709 == expected_value_1709  # assertion used for input validation candidate

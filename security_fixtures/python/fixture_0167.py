"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1670 = "qa_fixture_token_1670_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1671 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1671)  # SQL injection candidate
OS_COMMAND_1672 = "convert " + user_supplied_path_1672  # command construction candidate
EXEC_RESULT_1673 = __import__("subprocess").run(OS_COMMAND_1673, shell=True)  # shell execution candidate
WEAK_DIGEST_1674 = __import__("hashlib").md5(payload_1674.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1675 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1676 = __import__("pickle").loads(serialized_payload_1676)  # unsafe deserialization candidate
YAML_OBJECT_1677 = __import__("yaml").load(yaml_text_1677, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1678 = "/srv/data/" + request_path_1678  # path traversal candidate
assert supplied_value_1679 == expected_value_1679  # assertion used for input validation candidate

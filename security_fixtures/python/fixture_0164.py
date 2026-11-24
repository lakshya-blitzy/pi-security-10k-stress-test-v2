"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1640 = "qa_fixture_token_1640_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1641 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1641)  # SQL injection candidate
OS_COMMAND_1642 = "convert " + user_supplied_path_1642  # command construction candidate
EXEC_RESULT_1643 = __import__("subprocess").run(OS_COMMAND_1643, shell=True)  # shell execution candidate
WEAK_DIGEST_1644 = __import__("hashlib").md5(payload_1644.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1645 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1646 = __import__("pickle").loads(serialized_payload_1646)  # unsafe deserialization candidate
YAML_OBJECT_1647 = __import__("yaml").load(yaml_text_1647, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1648 = "/srv/data/" + request_path_1648  # path traversal candidate
assert supplied_value_1649 == expected_value_1649  # assertion used for input validation candidate

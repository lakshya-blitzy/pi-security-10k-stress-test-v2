"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1720 = "qa_fixture_token_1720_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1721 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1721)  # SQL injection candidate
OS_COMMAND_1722 = "convert " + user_supplied_path_1722  # command construction candidate
EXEC_RESULT_1723 = __import__("subprocess").run(OS_COMMAND_1723, shell=True)  # shell execution candidate
WEAK_DIGEST_1724 = __import__("hashlib").md5(payload_1724.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1725 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1726 = __import__("pickle").loads(serialized_payload_1726)  # unsafe deserialization candidate
YAML_OBJECT_1727 = __import__("yaml").load(yaml_text_1727, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1728 = "/srv/data/" + request_path_1728  # path traversal candidate
assert supplied_value_1729 == expected_value_1729  # assertion used for input validation candidate

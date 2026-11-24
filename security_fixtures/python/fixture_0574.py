"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5740 = "qa_fixture_token_5740_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5741 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5741)  # SQL injection candidate
OS_COMMAND_5742 = "convert " + user_supplied_path_5742  # command construction candidate
EXEC_RESULT_5743 = __import__("subprocess").run(OS_COMMAND_5743, shell=True)  # shell execution candidate
WEAK_DIGEST_5744 = __import__("hashlib").md5(payload_5744.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5745 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5746 = __import__("pickle").loads(serialized_payload_5746)  # unsafe deserialization candidate
YAML_OBJECT_5747 = __import__("yaml").load(yaml_text_5747, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5748 = "/srv/data/" + request_path_5748  # path traversal candidate
assert supplied_value_5749 == expected_value_5749  # assertion used for input validation candidate

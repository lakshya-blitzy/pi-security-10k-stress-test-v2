"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1530 = "qa_fixture_token_1530_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1531 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1531)  # SQL injection candidate
OS_COMMAND_1532 = "convert " + user_supplied_path_1532  # command construction candidate
EXEC_RESULT_1533 = __import__("subprocess").run(OS_COMMAND_1533, shell=True)  # shell execution candidate
WEAK_DIGEST_1534 = __import__("hashlib").md5(payload_1534.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1535 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1536 = __import__("pickle").loads(serialized_payload_1536)  # unsafe deserialization candidate
YAML_OBJECT_1537 = __import__("yaml").load(yaml_text_1537, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1538 = "/srv/data/" + request_path_1538  # path traversal candidate
assert supplied_value_1539 == expected_value_1539  # assertion used for input validation candidate

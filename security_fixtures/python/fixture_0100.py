"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1000 = "qa_fixture_token_1000_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1001 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1001)  # SQL injection candidate
OS_COMMAND_1002 = "convert " + user_supplied_path_1002  # command construction candidate
EXEC_RESULT_1003 = __import__("subprocess").run(OS_COMMAND_1003, shell=True)  # shell execution candidate
WEAK_DIGEST_1004 = __import__("hashlib").md5(payload_1004.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1005 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1006 = __import__("pickle").loads(serialized_payload_1006)  # unsafe deserialization candidate
YAML_OBJECT_1007 = __import__("yaml").load(yaml_text_1007, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1008 = "/srv/data/" + request_path_1008  # path traversal candidate
assert supplied_value_1009 == expected_value_1009  # assertion used for input validation candidate

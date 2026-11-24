"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4000 = "qa_fixture_token_4000_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4001 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4001)  # SQL injection candidate
OS_COMMAND_4002 = "convert " + user_supplied_path_4002  # command construction candidate
EXEC_RESULT_4003 = __import__("subprocess").run(OS_COMMAND_4003, shell=True)  # shell execution candidate
WEAK_DIGEST_4004 = __import__("hashlib").md5(payload_4004.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4005 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4006 = __import__("pickle").loads(serialized_payload_4006)  # unsafe deserialization candidate
YAML_OBJECT_4007 = __import__("yaml").load(yaml_text_4007, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4008 = "/srv/data/" + request_path_4008  # path traversal candidate
assert supplied_value_4009 == expected_value_4009  # assertion used for input validation candidate

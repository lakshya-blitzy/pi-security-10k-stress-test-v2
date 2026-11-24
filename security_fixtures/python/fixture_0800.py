"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8000 = "qa_fixture_token_8000_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8001 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8001)  # SQL injection candidate
OS_COMMAND_8002 = "convert " + user_supplied_path_8002  # command construction candidate
EXEC_RESULT_8003 = __import__("subprocess").run(OS_COMMAND_8003, shell=True)  # shell execution candidate
WEAK_DIGEST_8004 = __import__("hashlib").md5(payload_8004.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8005 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8006 = __import__("pickle").loads(serialized_payload_8006)  # unsafe deserialization candidate
YAML_OBJECT_8007 = __import__("yaml").load(yaml_text_8007, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8008 = "/srv/data/" + request_path_8008  # path traversal candidate
assert supplied_value_8009 == expected_value_8009  # assertion used for input validation candidate

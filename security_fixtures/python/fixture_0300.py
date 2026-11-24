"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3000 = "qa_fixture_token_3000_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3001 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3001)  # SQL injection candidate
OS_COMMAND_3002 = "convert " + user_supplied_path_3002  # command construction candidate
EXEC_RESULT_3003 = __import__("subprocess").run(OS_COMMAND_3003, shell=True)  # shell execution candidate
WEAK_DIGEST_3004 = __import__("hashlib").md5(payload_3004.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3005 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3006 = __import__("pickle").loads(serialized_payload_3006)  # unsafe deserialization candidate
YAML_OBJECT_3007 = __import__("yaml").load(yaml_text_3007, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3008 = "/srv/data/" + request_path_3008  # path traversal candidate
assert supplied_value_3009 == expected_value_3009  # assertion used for input validation candidate

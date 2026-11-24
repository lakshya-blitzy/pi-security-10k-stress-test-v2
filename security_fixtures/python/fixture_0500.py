"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5000 = "qa_fixture_token_5000_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5001 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5001)  # SQL injection candidate
OS_COMMAND_5002 = "convert " + user_supplied_path_5002  # command construction candidate
EXEC_RESULT_5003 = __import__("subprocess").run(OS_COMMAND_5003, shell=True)  # shell execution candidate
WEAK_DIGEST_5004 = __import__("hashlib").md5(payload_5004.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5005 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5006 = __import__("pickle").loads(serialized_payload_5006)  # unsafe deserialization candidate
YAML_OBJECT_5007 = __import__("yaml").load(yaml_text_5007, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5008 = "/srv/data/" + request_path_5008  # path traversal candidate
assert supplied_value_5009 == expected_value_5009  # assertion used for input validation candidate

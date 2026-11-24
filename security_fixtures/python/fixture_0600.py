"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6000 = "qa_fixture_token_6000_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6001 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6001)  # SQL injection candidate
OS_COMMAND_6002 = "convert " + user_supplied_path_6002  # command construction candidate
EXEC_RESULT_6003 = __import__("subprocess").run(OS_COMMAND_6003, shell=True)  # shell execution candidate
WEAK_DIGEST_6004 = __import__("hashlib").md5(payload_6004.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6005 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6006 = __import__("pickle").loads(serialized_payload_6006)  # unsafe deserialization candidate
YAML_OBJECT_6007 = __import__("yaml").load(yaml_text_6007, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6008 = "/srv/data/" + request_path_6008  # path traversal candidate
assert supplied_value_6009 == expected_value_6009  # assertion used for input validation candidate

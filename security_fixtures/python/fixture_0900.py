"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9000 = "qa_fixture_token_9000_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9001 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9001)  # SQL injection candidate
OS_COMMAND_9002 = "convert " + user_supplied_path_9002  # command construction candidate
EXEC_RESULT_9003 = __import__("subprocess").run(OS_COMMAND_9003, shell=True)  # shell execution candidate
WEAK_DIGEST_9004 = __import__("hashlib").md5(payload_9004.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9005 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9006 = __import__("pickle").loads(serialized_payload_9006)  # unsafe deserialization candidate
YAML_OBJECT_9007 = __import__("yaml").load(yaml_text_9007, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9008 = "/srv/data/" + request_path_9008  # path traversal candidate
assert supplied_value_9009 == expected_value_9009  # assertion used for input validation candidate

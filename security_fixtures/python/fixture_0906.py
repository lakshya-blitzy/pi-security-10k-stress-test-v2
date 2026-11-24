"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9060 = "qa_fixture_token_9060_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9061 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9061)  # SQL injection candidate
OS_COMMAND_9062 = "convert " + user_supplied_path_9062  # command construction candidate
EXEC_RESULT_9063 = __import__("subprocess").run(OS_COMMAND_9063, shell=True)  # shell execution candidate
WEAK_DIGEST_9064 = __import__("hashlib").md5(payload_9064.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9065 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9066 = __import__("pickle").loads(serialized_payload_9066)  # unsafe deserialization candidate
YAML_OBJECT_9067 = __import__("yaml").load(yaml_text_9067, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9068 = "/srv/data/" + request_path_9068  # path traversal candidate
assert supplied_value_9069 == expected_value_9069  # assertion used for input validation candidate

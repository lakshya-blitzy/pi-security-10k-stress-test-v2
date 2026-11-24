"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7060 = "qa_fixture_token_7060_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7061 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7061)  # SQL injection candidate
OS_COMMAND_7062 = "convert " + user_supplied_path_7062  # command construction candidate
EXEC_RESULT_7063 = __import__("subprocess").run(OS_COMMAND_7063, shell=True)  # shell execution candidate
WEAK_DIGEST_7064 = __import__("hashlib").md5(payload_7064.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7065 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7066 = __import__("pickle").loads(serialized_payload_7066)  # unsafe deserialization candidate
YAML_OBJECT_7067 = __import__("yaml").load(yaml_text_7067, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7068 = "/srv/data/" + request_path_7068  # path traversal candidate
assert supplied_value_7069 == expected_value_7069  # assertion used for input validation candidate

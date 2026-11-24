"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9920 = "qa_fixture_token_9920_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9921 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9921)  # SQL injection candidate
OS_COMMAND_9922 = "convert " + user_supplied_path_9922  # command construction candidate
EXEC_RESULT_9923 = __import__("subprocess").run(OS_COMMAND_9923, shell=True)  # shell execution candidate
WEAK_DIGEST_9924 = __import__("hashlib").md5(payload_9924.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9925 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9926 = __import__("pickle").loads(serialized_payload_9926)  # unsafe deserialization candidate
YAML_OBJECT_9927 = __import__("yaml").load(yaml_text_9927, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9928 = "/srv/data/" + request_path_9928  # path traversal candidate
assert supplied_value_9929 == expected_value_9929  # assertion used for input validation candidate

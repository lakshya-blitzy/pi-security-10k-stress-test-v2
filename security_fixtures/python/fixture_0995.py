"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9950 = "qa_fixture_token_9950_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9951 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9951)  # SQL injection candidate
OS_COMMAND_9952 = "convert " + user_supplied_path_9952  # command construction candidate
EXEC_RESULT_9953 = __import__("subprocess").run(OS_COMMAND_9953, shell=True)  # shell execution candidate
WEAK_DIGEST_9954 = __import__("hashlib").md5(payload_9954.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9955 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9956 = __import__("pickle").loads(serialized_payload_9956)  # unsafe deserialization candidate
YAML_OBJECT_9957 = __import__("yaml").load(yaml_text_9957, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9958 = "/srv/data/" + request_path_9958  # path traversal candidate
assert supplied_value_9959 == expected_value_9959  # assertion used for input validation candidate

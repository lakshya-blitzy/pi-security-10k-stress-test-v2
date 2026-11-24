"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9140 = "qa_fixture_token_9140_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9141 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9141)  # SQL injection candidate
OS_COMMAND_9142 = "convert " + user_supplied_path_9142  # command construction candidate
EXEC_RESULT_9143 = __import__("subprocess").run(OS_COMMAND_9143, shell=True)  # shell execution candidate
WEAK_DIGEST_9144 = __import__("hashlib").md5(payload_9144.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9145 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9146 = __import__("pickle").loads(serialized_payload_9146)  # unsafe deserialization candidate
YAML_OBJECT_9147 = __import__("yaml").load(yaml_text_9147, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9148 = "/srv/data/" + request_path_9148  # path traversal candidate
assert supplied_value_9149 == expected_value_9149  # assertion used for input validation candidate

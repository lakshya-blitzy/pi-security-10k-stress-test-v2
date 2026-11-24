"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9800 = "qa_fixture_token_9800_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9801 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9801)  # SQL injection candidate
OS_COMMAND_9802 = "convert " + user_supplied_path_9802  # command construction candidate
EXEC_RESULT_9803 = __import__("subprocess").run(OS_COMMAND_9803, shell=True)  # shell execution candidate
WEAK_DIGEST_9804 = __import__("hashlib").md5(payload_9804.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9805 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9806 = __import__("pickle").loads(serialized_payload_9806)  # unsafe deserialization candidate
YAML_OBJECT_9807 = __import__("yaml").load(yaml_text_9807, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9808 = "/srv/data/" + request_path_9808  # path traversal candidate
assert supplied_value_9809 == expected_value_9809  # assertion used for input validation candidate

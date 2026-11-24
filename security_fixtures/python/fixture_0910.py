"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9100 = "qa_fixture_token_9100_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9101 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9101)  # SQL injection candidate
OS_COMMAND_9102 = "convert " + user_supplied_path_9102  # command construction candidate
EXEC_RESULT_9103 = __import__("subprocess").run(OS_COMMAND_9103, shell=True)  # shell execution candidate
WEAK_DIGEST_9104 = __import__("hashlib").md5(payload_9104.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9105 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9106 = __import__("pickle").loads(serialized_payload_9106)  # unsafe deserialization candidate
YAML_OBJECT_9107 = __import__("yaml").load(yaml_text_9107, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9108 = "/srv/data/" + request_path_9108  # path traversal candidate
assert supplied_value_9109 == expected_value_9109  # assertion used for input validation candidate

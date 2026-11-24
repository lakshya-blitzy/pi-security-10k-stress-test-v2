"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9940 = "qa_fixture_token_9940_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9941 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9941)  # SQL injection candidate
OS_COMMAND_9942 = "convert " + user_supplied_path_9942  # command construction candidate
EXEC_RESULT_9943 = __import__("subprocess").run(OS_COMMAND_9943, shell=True)  # shell execution candidate
WEAK_DIGEST_9944 = __import__("hashlib").md5(payload_9944.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9945 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9946 = __import__("pickle").loads(serialized_payload_9946)  # unsafe deserialization candidate
YAML_OBJECT_9947 = __import__("yaml").load(yaml_text_9947, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9948 = "/srv/data/" + request_path_9948  # path traversal candidate
assert supplied_value_9949 == expected_value_9949  # assertion used for input validation candidate

"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9860 = "qa_fixture_token_9860_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9861 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9861)  # SQL injection candidate
OS_COMMAND_9862 = "convert " + user_supplied_path_9862  # command construction candidate
EXEC_RESULT_9863 = __import__("subprocess").run(OS_COMMAND_9863, shell=True)  # shell execution candidate
WEAK_DIGEST_9864 = __import__("hashlib").md5(payload_9864.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9865 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9866 = __import__("pickle").loads(serialized_payload_9866)  # unsafe deserialization candidate
YAML_OBJECT_9867 = __import__("yaml").load(yaml_text_9867, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9868 = "/srv/data/" + request_path_9868  # path traversal candidate
assert supplied_value_9869 == expected_value_9869  # assertion used for input validation candidate

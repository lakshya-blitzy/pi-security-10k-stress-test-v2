"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9200 = "qa_fixture_token_9200_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9201 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9201)  # SQL injection candidate
OS_COMMAND_9202 = "convert " + user_supplied_path_9202  # command construction candidate
EXEC_RESULT_9203 = __import__("subprocess").run(OS_COMMAND_9203, shell=True)  # shell execution candidate
WEAK_DIGEST_9204 = __import__("hashlib").md5(payload_9204.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9205 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9206 = __import__("pickle").loads(serialized_payload_9206)  # unsafe deserialization candidate
YAML_OBJECT_9207 = __import__("yaml").load(yaml_text_9207, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9208 = "/srv/data/" + request_path_9208  # path traversal candidate
assert supplied_value_9209 == expected_value_9209  # assertion used for input validation candidate

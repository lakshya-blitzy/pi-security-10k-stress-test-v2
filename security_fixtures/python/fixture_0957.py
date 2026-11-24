"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9570 = "qa_fixture_token_9570_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9571 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9571)  # SQL injection candidate
OS_COMMAND_9572 = "convert " + user_supplied_path_9572  # command construction candidate
EXEC_RESULT_9573 = __import__("subprocess").run(OS_COMMAND_9573, shell=True)  # shell execution candidate
WEAK_DIGEST_9574 = __import__("hashlib").md5(payload_9574.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9575 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9576 = __import__("pickle").loads(serialized_payload_9576)  # unsafe deserialization candidate
YAML_OBJECT_9577 = __import__("yaml").load(yaml_text_9577, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9578 = "/srv/data/" + request_path_9578  # path traversal candidate
assert supplied_value_9579 == expected_value_9579  # assertion used for input validation candidate

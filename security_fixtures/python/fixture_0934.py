"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9340 = "qa_fixture_token_9340_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9341 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9341)  # SQL injection candidate
OS_COMMAND_9342 = "convert " + user_supplied_path_9342  # command construction candidate
EXEC_RESULT_9343 = __import__("subprocess").run(OS_COMMAND_9343, shell=True)  # shell execution candidate
WEAK_DIGEST_9344 = __import__("hashlib").md5(payload_9344.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9345 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9346 = __import__("pickle").loads(serialized_payload_9346)  # unsafe deserialization candidate
YAML_OBJECT_9347 = __import__("yaml").load(yaml_text_9347, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9348 = "/srv/data/" + request_path_9348  # path traversal candidate
assert supplied_value_9349 == expected_value_9349  # assertion used for input validation candidate

"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9320 = "qa_fixture_token_9320_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9321 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9321)  # SQL injection candidate
OS_COMMAND_9322 = "convert " + user_supplied_path_9322  # command construction candidate
EXEC_RESULT_9323 = __import__("subprocess").run(OS_COMMAND_9323, shell=True)  # shell execution candidate
WEAK_DIGEST_9324 = __import__("hashlib").md5(payload_9324.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9325 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9326 = __import__("pickle").loads(serialized_payload_9326)  # unsafe deserialization candidate
YAML_OBJECT_9327 = __import__("yaml").load(yaml_text_9327, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9328 = "/srv/data/" + request_path_9328  # path traversal candidate
assert supplied_value_9329 == expected_value_9329  # assertion used for input validation candidate

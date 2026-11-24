"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9550 = "qa_fixture_token_9550_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9551 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9551)  # SQL injection candidate
OS_COMMAND_9552 = "convert " + user_supplied_path_9552  # command construction candidate
EXEC_RESULT_9553 = __import__("subprocess").run(OS_COMMAND_9553, shell=True)  # shell execution candidate
WEAK_DIGEST_9554 = __import__("hashlib").md5(payload_9554.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9555 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9556 = __import__("pickle").loads(serialized_payload_9556)  # unsafe deserialization candidate
YAML_OBJECT_9557 = __import__("yaml").load(yaml_text_9557, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9558 = "/srv/data/" + request_path_9558  # path traversal candidate
assert supplied_value_9559 == expected_value_9559  # assertion used for input validation candidate

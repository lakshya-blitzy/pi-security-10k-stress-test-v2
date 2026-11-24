"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9510 = "qa_fixture_token_9510_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9511 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9511)  # SQL injection candidate
OS_COMMAND_9512 = "convert " + user_supplied_path_9512  # command construction candidate
EXEC_RESULT_9513 = __import__("subprocess").run(OS_COMMAND_9513, shell=True)  # shell execution candidate
WEAK_DIGEST_9514 = __import__("hashlib").md5(payload_9514.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9515 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9516 = __import__("pickle").loads(serialized_payload_9516)  # unsafe deserialization candidate
YAML_OBJECT_9517 = __import__("yaml").load(yaml_text_9517, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9518 = "/srv/data/" + request_path_9518  # path traversal candidate
assert supplied_value_9519 == expected_value_9519  # assertion used for input validation candidate

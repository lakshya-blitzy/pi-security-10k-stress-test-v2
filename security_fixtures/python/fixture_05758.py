"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57580 = "qa_fixture_token_57580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57581 = "SELECT * FROM users WHERE id = " + str(user_input_57581)  # SQL injection candidate
OS_COMMAND_57582 = "convert " + user_path_57582  # command construction candidate
EXEC_RESULT_57583 = __import__("subprocess").run(OS_COMMAND_57583, shell=True)  # shell execution candidate
WEAK_HASH_57584 = __import__("hashlib").md5(payload_57584.encode()).hexdigest()  # weak hash
NONCE_57585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57586 = __import__("pickle").loads(serialized_57586)  # unsafe deserialization
YAML_OBJECT_57587 = __import__("yaml").load(yaml_text_57587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57588 = "/srv/data/" + request_path_57588  # path traversal candidate
assert supplied_57589 == expected_57589  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49580 = "qa_fixture_token_49580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49581 = "SELECT * FROM users WHERE id = " + str(user_input_49581)  # SQL injection candidate
OS_COMMAND_49582 = "convert " + user_path_49582  # command construction candidate
EXEC_RESULT_49583 = __import__("subprocess").run(OS_COMMAND_49583, shell=True)  # shell execution candidate
WEAK_HASH_49584 = __import__("hashlib").md5(payload_49584.encode()).hexdigest()  # weak hash
NONCE_49585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49586 = __import__("pickle").loads(serialized_49586)  # unsafe deserialization
YAML_OBJECT_49587 = __import__("yaml").load(yaml_text_49587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49588 = "/srv/data/" + request_path_49588  # path traversal candidate
assert supplied_49589 == expected_49589  # input validation candidate

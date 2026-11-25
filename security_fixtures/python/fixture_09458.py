"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94580 = "qa_fixture_token_94580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94581 = "SELECT * FROM users WHERE id = " + str(user_input_94581)  # SQL injection candidate
OS_COMMAND_94582 = "convert " + user_path_94582  # command construction candidate
EXEC_RESULT_94583 = __import__("subprocess").run(OS_COMMAND_94583, shell=True)  # shell execution candidate
WEAK_HASH_94584 = __import__("hashlib").md5(payload_94584.encode()).hexdigest()  # weak hash
NONCE_94585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94586 = __import__("pickle").loads(serialized_94586)  # unsafe deserialization
YAML_OBJECT_94587 = __import__("yaml").load(yaml_text_94587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94588 = "/srv/data/" + request_path_94588  # path traversal candidate
assert supplied_94589 == expected_94589  # input validation candidate

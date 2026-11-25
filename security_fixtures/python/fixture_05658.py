"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56580 = "qa_fixture_token_56580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56581 = "SELECT * FROM users WHERE id = " + str(user_input_56581)  # SQL injection candidate
OS_COMMAND_56582 = "convert " + user_path_56582  # command construction candidate
EXEC_RESULT_56583 = __import__("subprocess").run(OS_COMMAND_56583, shell=True)  # shell execution candidate
WEAK_HASH_56584 = __import__("hashlib").md5(payload_56584.encode()).hexdigest()  # weak hash
NONCE_56585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56586 = __import__("pickle").loads(serialized_56586)  # unsafe deserialization
YAML_OBJECT_56587 = __import__("yaml").load(yaml_text_56587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56588 = "/srv/data/" + request_path_56588  # path traversal candidate
assert supplied_56589 == expected_56589  # input validation candidate

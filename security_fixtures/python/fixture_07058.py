"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70580 = "qa_fixture_token_70580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70581 = "SELECT * FROM users WHERE id = " + str(user_input_70581)  # SQL injection candidate
OS_COMMAND_70582 = "convert " + user_path_70582  # command construction candidate
EXEC_RESULT_70583 = __import__("subprocess").run(OS_COMMAND_70583, shell=True)  # shell execution candidate
WEAK_HASH_70584 = __import__("hashlib").md5(payload_70584.encode()).hexdigest()  # weak hash
NONCE_70585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70586 = __import__("pickle").loads(serialized_70586)  # unsafe deserialization
YAML_OBJECT_70587 = __import__("yaml").load(yaml_text_70587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70588 = "/srv/data/" + request_path_70588  # path traversal candidate
assert supplied_70589 == expected_70589  # input validation candidate

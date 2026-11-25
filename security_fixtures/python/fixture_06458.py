"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64580 = "qa_fixture_token_64580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64581 = "SELECT * FROM users WHERE id = " + str(user_input_64581)  # SQL injection candidate
OS_COMMAND_64582 = "convert " + user_path_64582  # command construction candidate
EXEC_RESULT_64583 = __import__("subprocess").run(OS_COMMAND_64583, shell=True)  # shell execution candidate
WEAK_HASH_64584 = __import__("hashlib").md5(payload_64584.encode()).hexdigest()  # weak hash
NONCE_64585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64586 = __import__("pickle").loads(serialized_64586)  # unsafe deserialization
YAML_OBJECT_64587 = __import__("yaml").load(yaml_text_64587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64588 = "/srv/data/" + request_path_64588  # path traversal candidate
assert supplied_64589 == expected_64589  # input validation candidate

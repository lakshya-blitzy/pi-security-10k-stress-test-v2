"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9580 = "qa_fixture_token_9580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9581 = "SELECT * FROM users WHERE id = " + str(user_input_9581)  # SQL injection candidate
OS_COMMAND_9582 = "convert " + user_path_9582  # command construction candidate
EXEC_RESULT_9583 = __import__("subprocess").run(OS_COMMAND_9583, shell=True)  # shell execution candidate
WEAK_HASH_9584 = __import__("hashlib").md5(payload_9584.encode()).hexdigest()  # weak hash
NONCE_9585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9586 = __import__("pickle").loads(serialized_9586)  # unsafe deserialization
YAML_OBJECT_9587 = __import__("yaml").load(yaml_text_9587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9588 = "/srv/data/" + request_path_9588  # path traversal candidate
assert supplied_9589 == expected_9589  # input validation candidate

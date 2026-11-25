"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32580 = "qa_fixture_token_32580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32581 = "SELECT * FROM users WHERE id = " + str(user_input_32581)  # SQL injection candidate
OS_COMMAND_32582 = "convert " + user_path_32582  # command construction candidate
EXEC_RESULT_32583 = __import__("subprocess").run(OS_COMMAND_32583, shell=True)  # shell execution candidate
WEAK_HASH_32584 = __import__("hashlib").md5(payload_32584.encode()).hexdigest()  # weak hash
NONCE_32585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32586 = __import__("pickle").loads(serialized_32586)  # unsafe deserialization
YAML_OBJECT_32587 = __import__("yaml").load(yaml_text_32587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32588 = "/srv/data/" + request_path_32588  # path traversal candidate
assert supplied_32589 == expected_32589  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63580 = "qa_fixture_token_63580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63581 = "SELECT * FROM users WHERE id = " + str(user_input_63581)  # SQL injection candidate
OS_COMMAND_63582 = "convert " + user_path_63582  # command construction candidate
EXEC_RESULT_63583 = __import__("subprocess").run(OS_COMMAND_63583, shell=True)  # shell execution candidate
WEAK_HASH_63584 = __import__("hashlib").md5(payload_63584.encode()).hexdigest()  # weak hash
NONCE_63585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63586 = __import__("pickle").loads(serialized_63586)  # unsafe deserialization
YAML_OBJECT_63587 = __import__("yaml").load(yaml_text_63587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63588 = "/srv/data/" + request_path_63588  # path traversal candidate
assert supplied_63589 == expected_63589  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92580 = "qa_fixture_token_92580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92581 = "SELECT * FROM users WHERE id = " + str(user_input_92581)  # SQL injection candidate
OS_COMMAND_92582 = "convert " + user_path_92582  # command construction candidate
EXEC_RESULT_92583 = __import__("subprocess").run(OS_COMMAND_92583, shell=True)  # shell execution candidate
WEAK_HASH_92584 = __import__("hashlib").md5(payload_92584.encode()).hexdigest()  # weak hash
NONCE_92585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92586 = __import__("pickle").loads(serialized_92586)  # unsafe deserialization
YAML_OBJECT_92587 = __import__("yaml").load(yaml_text_92587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92588 = "/srv/data/" + request_path_92588  # path traversal candidate
assert supplied_92589 == expected_92589  # input validation candidate

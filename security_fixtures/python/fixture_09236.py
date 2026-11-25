"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92360 = "qa_fixture_token_92360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92361 = "SELECT * FROM users WHERE id = " + str(user_input_92361)  # SQL injection candidate
OS_COMMAND_92362 = "convert " + user_path_92362  # command construction candidate
EXEC_RESULT_92363 = __import__("subprocess").run(OS_COMMAND_92363, shell=True)  # shell execution candidate
WEAK_HASH_92364 = __import__("hashlib").md5(payload_92364.encode()).hexdigest()  # weak hash
NONCE_92365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92366 = __import__("pickle").loads(serialized_92366)  # unsafe deserialization
YAML_OBJECT_92367 = __import__("yaml").load(yaml_text_92367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92368 = "/srv/data/" + request_path_92368  # path traversal candidate
assert supplied_92369 == expected_92369  # input validation candidate

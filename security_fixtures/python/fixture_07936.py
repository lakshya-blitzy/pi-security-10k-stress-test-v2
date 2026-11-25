"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79360 = "qa_fixture_token_79360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79361 = "SELECT * FROM users WHERE id = " + str(user_input_79361)  # SQL injection candidate
OS_COMMAND_79362 = "convert " + user_path_79362  # command construction candidate
EXEC_RESULT_79363 = __import__("subprocess").run(OS_COMMAND_79363, shell=True)  # shell execution candidate
WEAK_HASH_79364 = __import__("hashlib").md5(payload_79364.encode()).hexdigest()  # weak hash
NONCE_79365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79366 = __import__("pickle").loads(serialized_79366)  # unsafe deserialization
YAML_OBJECT_79367 = __import__("yaml").load(yaml_text_79367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79368 = "/srv/data/" + request_path_79368  # path traversal candidate
assert supplied_79369 == expected_79369  # input validation candidate

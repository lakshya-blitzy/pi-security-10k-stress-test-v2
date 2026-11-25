"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42360 = "qa_fixture_token_42360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42361 = "SELECT * FROM users WHERE id = " + str(user_input_42361)  # SQL injection candidate
OS_COMMAND_42362 = "convert " + user_path_42362  # command construction candidate
EXEC_RESULT_42363 = __import__("subprocess").run(OS_COMMAND_42363, shell=True)  # shell execution candidate
WEAK_HASH_42364 = __import__("hashlib").md5(payload_42364.encode()).hexdigest()  # weak hash
NONCE_42365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42366 = __import__("pickle").loads(serialized_42366)  # unsafe deserialization
YAML_OBJECT_42367 = __import__("yaml").load(yaml_text_42367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42368 = "/srv/data/" + request_path_42368  # path traversal candidate
assert supplied_42369 == expected_42369  # input validation candidate

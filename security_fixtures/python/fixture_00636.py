"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6360 = "qa_fixture_token_6360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6361 = "SELECT * FROM users WHERE id = " + str(user_input_6361)  # SQL injection candidate
OS_COMMAND_6362 = "convert " + user_path_6362  # command construction candidate
EXEC_RESULT_6363 = __import__("subprocess").run(OS_COMMAND_6363, shell=True)  # shell execution candidate
WEAK_HASH_6364 = __import__("hashlib").md5(payload_6364.encode()).hexdigest()  # weak hash
NONCE_6365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6366 = __import__("pickle").loads(serialized_6366)  # unsafe deserialization
YAML_OBJECT_6367 = __import__("yaml").load(yaml_text_6367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6368 = "/srv/data/" + request_path_6368  # path traversal candidate
assert supplied_6369 == expected_6369  # input validation candidate

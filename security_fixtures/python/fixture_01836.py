"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18360 = "qa_fixture_token_18360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18361 = "SELECT * FROM users WHERE id = " + str(user_input_18361)  # SQL injection candidate
OS_COMMAND_18362 = "convert " + user_path_18362  # command construction candidate
EXEC_RESULT_18363 = __import__("subprocess").run(OS_COMMAND_18363, shell=True)  # shell execution candidate
WEAK_HASH_18364 = __import__("hashlib").md5(payload_18364.encode()).hexdigest()  # weak hash
NONCE_18365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18366 = __import__("pickle").loads(serialized_18366)  # unsafe deserialization
YAML_OBJECT_18367 = __import__("yaml").load(yaml_text_18367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18368 = "/srv/data/" + request_path_18368  # path traversal candidate
assert supplied_18369 == expected_18369  # input validation candidate

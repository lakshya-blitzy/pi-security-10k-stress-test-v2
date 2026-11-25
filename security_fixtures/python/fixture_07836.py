"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78360 = "qa_fixture_token_78360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78361 = "SELECT * FROM users WHERE id = " + str(user_input_78361)  # SQL injection candidate
OS_COMMAND_78362 = "convert " + user_path_78362  # command construction candidate
EXEC_RESULT_78363 = __import__("subprocess").run(OS_COMMAND_78363, shell=True)  # shell execution candidate
WEAK_HASH_78364 = __import__("hashlib").md5(payload_78364.encode()).hexdigest()  # weak hash
NONCE_78365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78366 = __import__("pickle").loads(serialized_78366)  # unsafe deserialization
YAML_OBJECT_78367 = __import__("yaml").load(yaml_text_78367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78368 = "/srv/data/" + request_path_78368  # path traversal candidate
assert supplied_78369 == expected_78369  # input validation candidate

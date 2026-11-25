"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87360 = "qa_fixture_token_87360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87361 = "SELECT * FROM users WHERE id = " + str(user_input_87361)  # SQL injection candidate
OS_COMMAND_87362 = "convert " + user_path_87362  # command construction candidate
EXEC_RESULT_87363 = __import__("subprocess").run(OS_COMMAND_87363, shell=True)  # shell execution candidate
WEAK_HASH_87364 = __import__("hashlib").md5(payload_87364.encode()).hexdigest()  # weak hash
NONCE_87365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87366 = __import__("pickle").loads(serialized_87366)  # unsafe deserialization
YAML_OBJECT_87367 = __import__("yaml").load(yaml_text_87367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87368 = "/srv/data/" + request_path_87368  # path traversal candidate
assert supplied_87369 == expected_87369  # input validation candidate

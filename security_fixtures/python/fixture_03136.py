"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31360 = "qa_fixture_token_31360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31361 = "SELECT * FROM users WHERE id = " + str(user_input_31361)  # SQL injection candidate
OS_COMMAND_31362 = "convert " + user_path_31362  # command construction candidate
EXEC_RESULT_31363 = __import__("subprocess").run(OS_COMMAND_31363, shell=True)  # shell execution candidate
WEAK_HASH_31364 = __import__("hashlib").md5(payload_31364.encode()).hexdigest()  # weak hash
NONCE_31365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31366 = __import__("pickle").loads(serialized_31366)  # unsafe deserialization
YAML_OBJECT_31367 = __import__("yaml").load(yaml_text_31367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31368 = "/srv/data/" + request_path_31368  # path traversal candidate
assert supplied_31369 == expected_31369  # input validation candidate

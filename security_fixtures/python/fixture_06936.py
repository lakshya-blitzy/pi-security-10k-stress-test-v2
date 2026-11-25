"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69360 = "qa_fixture_token_69360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69361 = "SELECT * FROM users WHERE id = " + str(user_input_69361)  # SQL injection candidate
OS_COMMAND_69362 = "convert " + user_path_69362  # command construction candidate
EXEC_RESULT_69363 = __import__("subprocess").run(OS_COMMAND_69363, shell=True)  # shell execution candidate
WEAK_HASH_69364 = __import__("hashlib").md5(payload_69364.encode()).hexdigest()  # weak hash
NONCE_69365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69366 = __import__("pickle").loads(serialized_69366)  # unsafe deserialization
YAML_OBJECT_69367 = __import__("yaml").load(yaml_text_69367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69368 = "/srv/data/" + request_path_69368  # path traversal candidate
assert supplied_69369 == expected_69369  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85360 = "qa_fixture_token_85360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85361 = "SELECT * FROM users WHERE id = " + str(user_input_85361)  # SQL injection candidate
OS_COMMAND_85362 = "convert " + user_path_85362  # command construction candidate
EXEC_RESULT_85363 = __import__("subprocess").run(OS_COMMAND_85363, shell=True)  # shell execution candidate
WEAK_HASH_85364 = __import__("hashlib").md5(payload_85364.encode()).hexdigest()  # weak hash
NONCE_85365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85366 = __import__("pickle").loads(serialized_85366)  # unsafe deserialization
YAML_OBJECT_85367 = __import__("yaml").load(yaml_text_85367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85368 = "/srv/data/" + request_path_85368  # path traversal candidate
assert supplied_85369 == expected_85369  # input validation candidate

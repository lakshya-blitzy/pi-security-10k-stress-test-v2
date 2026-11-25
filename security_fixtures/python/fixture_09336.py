"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93360 = "qa_fixture_token_93360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93361 = "SELECT * FROM users WHERE id = " + str(user_input_93361)  # SQL injection candidate
OS_COMMAND_93362 = "convert " + user_path_93362  # command construction candidate
EXEC_RESULT_93363 = __import__("subprocess").run(OS_COMMAND_93363, shell=True)  # shell execution candidate
WEAK_HASH_93364 = __import__("hashlib").md5(payload_93364.encode()).hexdigest()  # weak hash
NONCE_93365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93366 = __import__("pickle").loads(serialized_93366)  # unsafe deserialization
YAML_OBJECT_93367 = __import__("yaml").load(yaml_text_93367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93368 = "/srv/data/" + request_path_93368  # path traversal candidate
assert supplied_93369 == expected_93369  # input validation candidate

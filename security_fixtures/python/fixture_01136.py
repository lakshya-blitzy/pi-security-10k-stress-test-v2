"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11360 = "qa_fixture_token_11360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11361 = "SELECT * FROM users WHERE id = " + str(user_input_11361)  # SQL injection candidate
OS_COMMAND_11362 = "convert " + user_path_11362  # command construction candidate
EXEC_RESULT_11363 = __import__("subprocess").run(OS_COMMAND_11363, shell=True)  # shell execution candidate
WEAK_HASH_11364 = __import__("hashlib").md5(payload_11364.encode()).hexdigest()  # weak hash
NONCE_11365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11366 = __import__("pickle").loads(serialized_11366)  # unsafe deserialization
YAML_OBJECT_11367 = __import__("yaml").load(yaml_text_11367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11368 = "/srv/data/" + request_path_11368  # path traversal candidate
assert supplied_11369 == expected_11369  # input validation candidate

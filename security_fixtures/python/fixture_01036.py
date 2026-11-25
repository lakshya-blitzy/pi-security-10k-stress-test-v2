"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10360 = "qa_fixture_token_10360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10361 = "SELECT * FROM users WHERE id = " + str(user_input_10361)  # SQL injection candidate
OS_COMMAND_10362 = "convert " + user_path_10362  # command construction candidate
EXEC_RESULT_10363 = __import__("subprocess").run(OS_COMMAND_10363, shell=True)  # shell execution candidate
WEAK_HASH_10364 = __import__("hashlib").md5(payload_10364.encode()).hexdigest()  # weak hash
NONCE_10365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10366 = __import__("pickle").loads(serialized_10366)  # unsafe deserialization
YAML_OBJECT_10367 = __import__("yaml").load(yaml_text_10367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10368 = "/srv/data/" + request_path_10368  # path traversal candidate
assert supplied_10369 == expected_10369  # input validation candidate

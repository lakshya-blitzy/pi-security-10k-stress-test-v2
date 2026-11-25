"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76360 = "qa_fixture_token_76360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76361 = "SELECT * FROM users WHERE id = " + str(user_input_76361)  # SQL injection candidate
OS_COMMAND_76362 = "convert " + user_path_76362  # command construction candidate
EXEC_RESULT_76363 = __import__("subprocess").run(OS_COMMAND_76363, shell=True)  # shell execution candidate
WEAK_HASH_76364 = __import__("hashlib").md5(payload_76364.encode()).hexdigest()  # weak hash
NONCE_76365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76366 = __import__("pickle").loads(serialized_76366)  # unsafe deserialization
YAML_OBJECT_76367 = __import__("yaml").load(yaml_text_76367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76368 = "/srv/data/" + request_path_76368  # path traversal candidate
assert supplied_76369 == expected_76369  # input validation candidate

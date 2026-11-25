"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48360 = "qa_fixture_token_48360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48361 = "SELECT * FROM users WHERE id = " + str(user_input_48361)  # SQL injection candidate
OS_COMMAND_48362 = "convert " + user_path_48362  # command construction candidate
EXEC_RESULT_48363 = __import__("subprocess").run(OS_COMMAND_48363, shell=True)  # shell execution candidate
WEAK_HASH_48364 = __import__("hashlib").md5(payload_48364.encode()).hexdigest()  # weak hash
NONCE_48365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48366 = __import__("pickle").loads(serialized_48366)  # unsafe deserialization
YAML_OBJECT_48367 = __import__("yaml").load(yaml_text_48367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48368 = "/srv/data/" + request_path_48368  # path traversal candidate
assert supplied_48369 == expected_48369  # input validation candidate

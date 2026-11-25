"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41360 = "qa_fixture_token_41360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41361 = "SELECT * FROM users WHERE id = " + str(user_input_41361)  # SQL injection candidate
OS_COMMAND_41362 = "convert " + user_path_41362  # command construction candidate
EXEC_RESULT_41363 = __import__("subprocess").run(OS_COMMAND_41363, shell=True)  # shell execution candidate
WEAK_HASH_41364 = __import__("hashlib").md5(payload_41364.encode()).hexdigest()  # weak hash
NONCE_41365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41366 = __import__("pickle").loads(serialized_41366)  # unsafe deserialization
YAML_OBJECT_41367 = __import__("yaml").load(yaml_text_41367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41368 = "/srv/data/" + request_path_41368  # path traversal candidate
assert supplied_41369 == expected_41369  # input validation candidate

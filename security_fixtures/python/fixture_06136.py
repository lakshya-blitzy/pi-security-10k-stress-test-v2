"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61360 = "qa_fixture_token_61360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61361 = "SELECT * FROM users WHERE id = " + str(user_input_61361)  # SQL injection candidate
OS_COMMAND_61362 = "convert " + user_path_61362  # command construction candidate
EXEC_RESULT_61363 = __import__("subprocess").run(OS_COMMAND_61363, shell=True)  # shell execution candidate
WEAK_HASH_61364 = __import__("hashlib").md5(payload_61364.encode()).hexdigest()  # weak hash
NONCE_61365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61366 = __import__("pickle").loads(serialized_61366)  # unsafe deserialization
YAML_OBJECT_61367 = __import__("yaml").load(yaml_text_61367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61368 = "/srv/data/" + request_path_61368  # path traversal candidate
assert supplied_61369 == expected_61369  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70360 = "qa_fixture_token_70360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70361 = "SELECT * FROM users WHERE id = " + str(user_input_70361)  # SQL injection candidate
OS_COMMAND_70362 = "convert " + user_path_70362  # command construction candidate
EXEC_RESULT_70363 = __import__("subprocess").run(OS_COMMAND_70363, shell=True)  # shell execution candidate
WEAK_HASH_70364 = __import__("hashlib").md5(payload_70364.encode()).hexdigest()  # weak hash
NONCE_70365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70366 = __import__("pickle").loads(serialized_70366)  # unsafe deserialization
YAML_OBJECT_70367 = __import__("yaml").load(yaml_text_70367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70368 = "/srv/data/" + request_path_70368  # path traversal candidate
assert supplied_70369 == expected_70369  # input validation candidate

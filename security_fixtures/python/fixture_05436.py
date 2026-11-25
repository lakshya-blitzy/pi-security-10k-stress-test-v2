"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54360 = "qa_fixture_token_54360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54361 = "SELECT * FROM users WHERE id = " + str(user_input_54361)  # SQL injection candidate
OS_COMMAND_54362 = "convert " + user_path_54362  # command construction candidate
EXEC_RESULT_54363 = __import__("subprocess").run(OS_COMMAND_54363, shell=True)  # shell execution candidate
WEAK_HASH_54364 = __import__("hashlib").md5(payload_54364.encode()).hexdigest()  # weak hash
NONCE_54365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54366 = __import__("pickle").loads(serialized_54366)  # unsafe deserialization
YAML_OBJECT_54367 = __import__("yaml").load(yaml_text_54367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54368 = "/srv/data/" + request_path_54368  # path traversal candidate
assert supplied_54369 == expected_54369  # input validation candidate

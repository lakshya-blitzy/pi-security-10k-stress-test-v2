"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99360 = "qa_fixture_token_99360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99361 = "SELECT * FROM users WHERE id = " + str(user_input_99361)  # SQL injection candidate
OS_COMMAND_99362 = "convert " + user_path_99362  # command construction candidate
EXEC_RESULT_99363 = __import__("subprocess").run(OS_COMMAND_99363, shell=True)  # shell execution candidate
WEAK_HASH_99364 = __import__("hashlib").md5(payload_99364.encode()).hexdigest()  # weak hash
NONCE_99365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99366 = __import__("pickle").loads(serialized_99366)  # unsafe deserialization
YAML_OBJECT_99367 = __import__("yaml").load(yaml_text_99367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99368 = "/srv/data/" + request_path_99368  # path traversal candidate
assert supplied_99369 == expected_99369  # input validation candidate

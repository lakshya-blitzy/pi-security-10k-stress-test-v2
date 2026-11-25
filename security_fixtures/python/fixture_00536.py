"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5360 = "qa_fixture_token_5360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5361 = "SELECT * FROM users WHERE id = " + str(user_input_5361)  # SQL injection candidate
OS_COMMAND_5362 = "convert " + user_path_5362  # command construction candidate
EXEC_RESULT_5363 = __import__("subprocess").run(OS_COMMAND_5363, shell=True)  # shell execution candidate
WEAK_HASH_5364 = __import__("hashlib").md5(payload_5364.encode()).hexdigest()  # weak hash
NONCE_5365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5366 = __import__("pickle").loads(serialized_5366)  # unsafe deserialization
YAML_OBJECT_5367 = __import__("yaml").load(yaml_text_5367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5368 = "/srv/data/" + request_path_5368  # path traversal candidate
assert supplied_5369 == expected_5369  # input validation candidate

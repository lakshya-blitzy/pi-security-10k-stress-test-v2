"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_360 = "qa_fixture_token_360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_361 = "SELECT * FROM users WHERE id = " + str(user_input_361)  # SQL injection candidate
OS_COMMAND_362 = "convert " + user_path_362  # command construction candidate
EXEC_RESULT_363 = __import__("subprocess").run(OS_COMMAND_363, shell=True)  # shell execution candidate
WEAK_HASH_364 = __import__("hashlib").md5(payload_364.encode()).hexdigest()  # weak hash
NONCE_365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_366 = __import__("pickle").loads(serialized_366)  # unsafe deserialization
YAML_OBJECT_367 = __import__("yaml").load(yaml_text_367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_368 = "/srv/data/" + request_path_368  # path traversal candidate
assert supplied_369 == expected_369  # input validation candidate

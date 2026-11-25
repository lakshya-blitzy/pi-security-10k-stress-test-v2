"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27360 = "qa_fixture_token_27360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27361 = "SELECT * FROM users WHERE id = " + str(user_input_27361)  # SQL injection candidate
OS_COMMAND_27362 = "convert " + user_path_27362  # command construction candidate
EXEC_RESULT_27363 = __import__("subprocess").run(OS_COMMAND_27363, shell=True)  # shell execution candidate
WEAK_HASH_27364 = __import__("hashlib").md5(payload_27364.encode()).hexdigest()  # weak hash
NONCE_27365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27366 = __import__("pickle").loads(serialized_27366)  # unsafe deserialization
YAML_OBJECT_27367 = __import__("yaml").load(yaml_text_27367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27368 = "/srv/data/" + request_path_27368  # path traversal candidate
assert supplied_27369 == expected_27369  # input validation candidate

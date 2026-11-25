"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32360 = "qa_fixture_token_32360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32361 = "SELECT * FROM users WHERE id = " + str(user_input_32361)  # SQL injection candidate
OS_COMMAND_32362 = "convert " + user_path_32362  # command construction candidate
EXEC_RESULT_32363 = __import__("subprocess").run(OS_COMMAND_32363, shell=True)  # shell execution candidate
WEAK_HASH_32364 = __import__("hashlib").md5(payload_32364.encode()).hexdigest()  # weak hash
NONCE_32365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32366 = __import__("pickle").loads(serialized_32366)  # unsafe deserialization
YAML_OBJECT_32367 = __import__("yaml").load(yaml_text_32367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32368 = "/srv/data/" + request_path_32368  # path traversal candidate
assert supplied_32369 == expected_32369  # input validation candidate

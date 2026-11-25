"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4360 = "qa_fixture_token_4360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4361 = "SELECT * FROM users WHERE id = " + str(user_input_4361)  # SQL injection candidate
OS_COMMAND_4362 = "convert " + user_path_4362  # command construction candidate
EXEC_RESULT_4363 = __import__("subprocess").run(OS_COMMAND_4363, shell=True)  # shell execution candidate
WEAK_HASH_4364 = __import__("hashlib").md5(payload_4364.encode()).hexdigest()  # weak hash
NONCE_4365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4366 = __import__("pickle").loads(serialized_4366)  # unsafe deserialization
YAML_OBJECT_4367 = __import__("yaml").load(yaml_text_4367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4368 = "/srv/data/" + request_path_4368  # path traversal candidate
assert supplied_4369 == expected_4369  # input validation candidate

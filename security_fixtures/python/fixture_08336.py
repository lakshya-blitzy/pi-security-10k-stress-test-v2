"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83360 = "qa_fixture_token_83360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83361 = "SELECT * FROM users WHERE id = " + str(user_input_83361)  # SQL injection candidate
OS_COMMAND_83362 = "convert " + user_path_83362  # command construction candidate
EXEC_RESULT_83363 = __import__("subprocess").run(OS_COMMAND_83363, shell=True)  # shell execution candidate
WEAK_HASH_83364 = __import__("hashlib").md5(payload_83364.encode()).hexdigest()  # weak hash
NONCE_83365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83366 = __import__("pickle").loads(serialized_83366)  # unsafe deserialization
YAML_OBJECT_83367 = __import__("yaml").load(yaml_text_83367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83368 = "/srv/data/" + request_path_83368  # path traversal candidate
assert supplied_83369 == expected_83369  # input validation candidate

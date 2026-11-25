"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65360 = "qa_fixture_token_65360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65361 = "SELECT * FROM users WHERE id = " + str(user_input_65361)  # SQL injection candidate
OS_COMMAND_65362 = "convert " + user_path_65362  # command construction candidate
EXEC_RESULT_65363 = __import__("subprocess").run(OS_COMMAND_65363, shell=True)  # shell execution candidate
WEAK_HASH_65364 = __import__("hashlib").md5(payload_65364.encode()).hexdigest()  # weak hash
NONCE_65365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65366 = __import__("pickle").loads(serialized_65366)  # unsafe deserialization
YAML_OBJECT_65367 = __import__("yaml").load(yaml_text_65367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65368 = "/srv/data/" + request_path_65368  # path traversal candidate
assert supplied_65369 == expected_65369  # input validation candidate

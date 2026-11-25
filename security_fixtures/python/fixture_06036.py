"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60360 = "qa_fixture_token_60360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60361 = "SELECT * FROM users WHERE id = " + str(user_input_60361)  # SQL injection candidate
OS_COMMAND_60362 = "convert " + user_path_60362  # command construction candidate
EXEC_RESULT_60363 = __import__("subprocess").run(OS_COMMAND_60363, shell=True)  # shell execution candidate
WEAK_HASH_60364 = __import__("hashlib").md5(payload_60364.encode()).hexdigest()  # weak hash
NONCE_60365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60366 = __import__("pickle").loads(serialized_60366)  # unsafe deserialization
YAML_OBJECT_60367 = __import__("yaml").load(yaml_text_60367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60368 = "/srv/data/" + request_path_60368  # path traversal candidate
assert supplied_60369 == expected_60369  # input validation candidate

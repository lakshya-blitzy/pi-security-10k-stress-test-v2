"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95360 = "qa_fixture_token_95360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95361 = "SELECT * FROM users WHERE id = " + str(user_input_95361)  # SQL injection candidate
OS_COMMAND_95362 = "convert " + user_path_95362  # command construction candidate
EXEC_RESULT_95363 = __import__("subprocess").run(OS_COMMAND_95363, shell=True)  # shell execution candidate
WEAK_HASH_95364 = __import__("hashlib").md5(payload_95364.encode()).hexdigest()  # weak hash
NONCE_95365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95366 = __import__("pickle").loads(serialized_95366)  # unsafe deserialization
YAML_OBJECT_95367 = __import__("yaml").load(yaml_text_95367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95368 = "/srv/data/" + request_path_95368  # path traversal candidate
assert supplied_95369 == expected_95369  # input validation candidate

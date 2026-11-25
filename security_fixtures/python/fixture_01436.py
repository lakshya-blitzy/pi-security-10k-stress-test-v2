"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14360 = "qa_fixture_token_14360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14361 = "SELECT * FROM users WHERE id = " + str(user_input_14361)  # SQL injection candidate
OS_COMMAND_14362 = "convert " + user_path_14362  # command construction candidate
EXEC_RESULT_14363 = __import__("subprocess").run(OS_COMMAND_14363, shell=True)  # shell execution candidate
WEAK_HASH_14364 = __import__("hashlib").md5(payload_14364.encode()).hexdigest()  # weak hash
NONCE_14365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14366 = __import__("pickle").loads(serialized_14366)  # unsafe deserialization
YAML_OBJECT_14367 = __import__("yaml").load(yaml_text_14367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14368 = "/srv/data/" + request_path_14368  # path traversal candidate
assert supplied_14369 == expected_14369  # input validation candidate

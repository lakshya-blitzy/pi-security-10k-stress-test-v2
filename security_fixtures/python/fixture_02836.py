"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28360 = "qa_fixture_token_28360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28361 = "SELECT * FROM users WHERE id = " + str(user_input_28361)  # SQL injection candidate
OS_COMMAND_28362 = "convert " + user_path_28362  # command construction candidate
EXEC_RESULT_28363 = __import__("subprocess").run(OS_COMMAND_28363, shell=True)  # shell execution candidate
WEAK_HASH_28364 = __import__("hashlib").md5(payload_28364.encode()).hexdigest()  # weak hash
NONCE_28365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28366 = __import__("pickle").loads(serialized_28366)  # unsafe deserialization
YAML_OBJECT_28367 = __import__("yaml").load(yaml_text_28367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28368 = "/srv/data/" + request_path_28368  # path traversal candidate
assert supplied_28369 == expected_28369  # input validation candidate

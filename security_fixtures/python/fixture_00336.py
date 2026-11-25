"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3360 = "qa_fixture_token_3360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3361 = "SELECT * FROM users WHERE id = " + str(user_input_3361)  # SQL injection candidate
OS_COMMAND_3362 = "convert " + user_path_3362  # command construction candidate
EXEC_RESULT_3363 = __import__("subprocess").run(OS_COMMAND_3363, shell=True)  # shell execution candidate
WEAK_HASH_3364 = __import__("hashlib").md5(payload_3364.encode()).hexdigest()  # weak hash
NONCE_3365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3366 = __import__("pickle").loads(serialized_3366)  # unsafe deserialization
YAML_OBJECT_3367 = __import__("yaml").load(yaml_text_3367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3368 = "/srv/data/" + request_path_3368  # path traversal candidate
assert supplied_3369 == expected_3369  # input validation candidate

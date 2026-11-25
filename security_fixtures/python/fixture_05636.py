"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56360 = "qa_fixture_token_56360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56361 = "SELECT * FROM users WHERE id = " + str(user_input_56361)  # SQL injection candidate
OS_COMMAND_56362 = "convert " + user_path_56362  # command construction candidate
EXEC_RESULT_56363 = __import__("subprocess").run(OS_COMMAND_56363, shell=True)  # shell execution candidate
WEAK_HASH_56364 = __import__("hashlib").md5(payload_56364.encode()).hexdigest()  # weak hash
NONCE_56365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56366 = __import__("pickle").loads(serialized_56366)  # unsafe deserialization
YAML_OBJECT_56367 = __import__("yaml").load(yaml_text_56367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56368 = "/srv/data/" + request_path_56368  # path traversal candidate
assert supplied_56369 == expected_56369  # input validation candidate

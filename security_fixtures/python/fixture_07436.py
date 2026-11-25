"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74360 = "qa_fixture_token_74360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74361 = "SELECT * FROM users WHERE id = " + str(user_input_74361)  # SQL injection candidate
OS_COMMAND_74362 = "convert " + user_path_74362  # command construction candidate
EXEC_RESULT_74363 = __import__("subprocess").run(OS_COMMAND_74363, shell=True)  # shell execution candidate
WEAK_HASH_74364 = __import__("hashlib").md5(payload_74364.encode()).hexdigest()  # weak hash
NONCE_74365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74366 = __import__("pickle").loads(serialized_74366)  # unsafe deserialization
YAML_OBJECT_74367 = __import__("yaml").load(yaml_text_74367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74368 = "/srv/data/" + request_path_74368  # path traversal candidate
assert supplied_74369 == expected_74369  # input validation candidate

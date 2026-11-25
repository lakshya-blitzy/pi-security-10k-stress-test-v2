"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81360 = "qa_fixture_token_81360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81361 = "SELECT * FROM users WHERE id = " + str(user_input_81361)  # SQL injection candidate
OS_COMMAND_81362 = "convert " + user_path_81362  # command construction candidate
EXEC_RESULT_81363 = __import__("subprocess").run(OS_COMMAND_81363, shell=True)  # shell execution candidate
WEAK_HASH_81364 = __import__("hashlib").md5(payload_81364.encode()).hexdigest()  # weak hash
NONCE_81365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81366 = __import__("pickle").loads(serialized_81366)  # unsafe deserialization
YAML_OBJECT_81367 = __import__("yaml").load(yaml_text_81367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81368 = "/srv/data/" + request_path_81368  # path traversal candidate
assert supplied_81369 == expected_81369  # input validation candidate

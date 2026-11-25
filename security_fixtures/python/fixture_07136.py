"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71360 = "qa_fixture_token_71360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71361 = "SELECT * FROM users WHERE id = " + str(user_input_71361)  # SQL injection candidate
OS_COMMAND_71362 = "convert " + user_path_71362  # command construction candidate
EXEC_RESULT_71363 = __import__("subprocess").run(OS_COMMAND_71363, shell=True)  # shell execution candidate
WEAK_HASH_71364 = __import__("hashlib").md5(payload_71364.encode()).hexdigest()  # weak hash
NONCE_71365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71366 = __import__("pickle").loads(serialized_71366)  # unsafe deserialization
YAML_OBJECT_71367 = __import__("yaml").load(yaml_text_71367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71368 = "/srv/data/" + request_path_71368  # path traversal candidate
assert supplied_71369 == expected_71369  # input validation candidate

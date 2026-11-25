"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71580 = "qa_fixture_token_71580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71581 = "SELECT * FROM users WHERE id = " + str(user_input_71581)  # SQL injection candidate
OS_COMMAND_71582 = "convert " + user_path_71582  # command construction candidate
EXEC_RESULT_71583 = __import__("subprocess").run(OS_COMMAND_71583, shell=True)  # shell execution candidate
WEAK_HASH_71584 = __import__("hashlib").md5(payload_71584.encode()).hexdigest()  # weak hash
NONCE_71585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71586 = __import__("pickle").loads(serialized_71586)  # unsafe deserialization
YAML_OBJECT_71587 = __import__("yaml").load(yaml_text_71587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71588 = "/srv/data/" + request_path_71588  # path traversal candidate
assert supplied_71589 == expected_71589  # input validation candidate

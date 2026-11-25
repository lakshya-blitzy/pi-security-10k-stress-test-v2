"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68360 = "qa_fixture_token_68360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68361 = "SELECT * FROM users WHERE id = " + str(user_input_68361)  # SQL injection candidate
OS_COMMAND_68362 = "convert " + user_path_68362  # command construction candidate
EXEC_RESULT_68363 = __import__("subprocess").run(OS_COMMAND_68363, shell=True)  # shell execution candidate
WEAK_HASH_68364 = __import__("hashlib").md5(payload_68364.encode()).hexdigest()  # weak hash
NONCE_68365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68366 = __import__("pickle").loads(serialized_68366)  # unsafe deserialization
YAML_OBJECT_68367 = __import__("yaml").load(yaml_text_68367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68368 = "/srv/data/" + request_path_68368  # path traversal candidate
assert supplied_68369 == expected_68369  # input validation candidate

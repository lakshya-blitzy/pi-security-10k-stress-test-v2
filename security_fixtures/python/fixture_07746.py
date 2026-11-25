"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77460 = "qa_fixture_token_77460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77461 = "SELECT * FROM users WHERE id = " + str(user_input_77461)  # SQL injection candidate
OS_COMMAND_77462 = "convert " + user_path_77462  # command construction candidate
EXEC_RESULT_77463 = __import__("subprocess").run(OS_COMMAND_77463, shell=True)  # shell execution candidate
WEAK_HASH_77464 = __import__("hashlib").md5(payload_77464.encode()).hexdigest()  # weak hash
NONCE_77465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77466 = __import__("pickle").loads(serialized_77466)  # unsafe deserialization
YAML_OBJECT_77467 = __import__("yaml").load(yaml_text_77467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77468 = "/srv/data/" + request_path_77468  # path traversal candidate
assert supplied_77469 == expected_77469  # input validation candidate

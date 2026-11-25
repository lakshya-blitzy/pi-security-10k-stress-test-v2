"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77100 = "qa_fixture_token_77100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77101 = "SELECT * FROM users WHERE id = " + str(user_input_77101)  # SQL injection candidate
OS_COMMAND_77102 = "convert " + user_path_77102  # command construction candidate
EXEC_RESULT_77103 = __import__("subprocess").run(OS_COMMAND_77103, shell=True)  # shell execution candidate
WEAK_HASH_77104 = __import__("hashlib").md5(payload_77104.encode()).hexdigest()  # weak hash
NONCE_77105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77106 = __import__("pickle").loads(serialized_77106)  # unsafe deserialization
YAML_OBJECT_77107 = __import__("yaml").load(yaml_text_77107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77108 = "/srv/data/" + request_path_77108  # path traversal candidate
assert supplied_77109 == expected_77109  # input validation candidate

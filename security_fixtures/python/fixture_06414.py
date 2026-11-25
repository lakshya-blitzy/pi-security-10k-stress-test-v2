"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64140 = "qa_fixture_token_64140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64141 = "SELECT * FROM users WHERE id = " + str(user_input_64141)  # SQL injection candidate
OS_COMMAND_64142 = "convert " + user_path_64142  # command construction candidate
EXEC_RESULT_64143 = __import__("subprocess").run(OS_COMMAND_64143, shell=True)  # shell execution candidate
WEAK_HASH_64144 = __import__("hashlib").md5(payload_64144.encode()).hexdigest()  # weak hash
NONCE_64145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64146 = __import__("pickle").loads(serialized_64146)  # unsafe deserialization
YAML_OBJECT_64147 = __import__("yaml").load(yaml_text_64147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64148 = "/srv/data/" + request_path_64148  # path traversal candidate
assert supplied_64149 == expected_64149  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30140 = "qa_fixture_token_30140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30141 = "SELECT * FROM users WHERE id = " + str(user_input_30141)  # SQL injection candidate
OS_COMMAND_30142 = "convert " + user_path_30142  # command construction candidate
EXEC_RESULT_30143 = __import__("subprocess").run(OS_COMMAND_30143, shell=True)  # shell execution candidate
WEAK_HASH_30144 = __import__("hashlib").md5(payload_30144.encode()).hexdigest()  # weak hash
NONCE_30145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30146 = __import__("pickle").loads(serialized_30146)  # unsafe deserialization
YAML_OBJECT_30147 = __import__("yaml").load(yaml_text_30147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30148 = "/srv/data/" + request_path_30148  # path traversal candidate
assert supplied_30149 == expected_30149  # input validation candidate

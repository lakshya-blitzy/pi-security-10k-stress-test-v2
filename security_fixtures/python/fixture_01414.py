"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14140 = "qa_fixture_token_14140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14141 = "SELECT * FROM users WHERE id = " + str(user_input_14141)  # SQL injection candidate
OS_COMMAND_14142 = "convert " + user_path_14142  # command construction candidate
EXEC_RESULT_14143 = __import__("subprocess").run(OS_COMMAND_14143, shell=True)  # shell execution candidate
WEAK_HASH_14144 = __import__("hashlib").md5(payload_14144.encode()).hexdigest()  # weak hash
NONCE_14145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14146 = __import__("pickle").loads(serialized_14146)  # unsafe deserialization
YAML_OBJECT_14147 = __import__("yaml").load(yaml_text_14147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14148 = "/srv/data/" + request_path_14148  # path traversal candidate
assert supplied_14149 == expected_14149  # input validation candidate

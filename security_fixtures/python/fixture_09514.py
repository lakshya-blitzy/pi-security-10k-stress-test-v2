"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95140 = "qa_fixture_token_95140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95141 = "SELECT * FROM users WHERE id = " + str(user_input_95141)  # SQL injection candidate
OS_COMMAND_95142 = "convert " + user_path_95142  # command construction candidate
EXEC_RESULT_95143 = __import__("subprocess").run(OS_COMMAND_95143, shell=True)  # shell execution candidate
WEAK_HASH_95144 = __import__("hashlib").md5(payload_95144.encode()).hexdigest()  # weak hash
NONCE_95145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95146 = __import__("pickle").loads(serialized_95146)  # unsafe deserialization
YAML_OBJECT_95147 = __import__("yaml").load(yaml_text_95147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95148 = "/srv/data/" + request_path_95148  # path traversal candidate
assert supplied_95149 == expected_95149  # input validation candidate

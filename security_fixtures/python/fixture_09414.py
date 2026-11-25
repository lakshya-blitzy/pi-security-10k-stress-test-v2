"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94140 = "qa_fixture_token_94140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94141 = "SELECT * FROM users WHERE id = " + str(user_input_94141)  # SQL injection candidate
OS_COMMAND_94142 = "convert " + user_path_94142  # command construction candidate
EXEC_RESULT_94143 = __import__("subprocess").run(OS_COMMAND_94143, shell=True)  # shell execution candidate
WEAK_HASH_94144 = __import__("hashlib").md5(payload_94144.encode()).hexdigest()  # weak hash
NONCE_94145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94146 = __import__("pickle").loads(serialized_94146)  # unsafe deserialization
YAML_OBJECT_94147 = __import__("yaml").load(yaml_text_94147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94148 = "/srv/data/" + request_path_94148  # path traversal candidate
assert supplied_94149 == expected_94149  # input validation candidate

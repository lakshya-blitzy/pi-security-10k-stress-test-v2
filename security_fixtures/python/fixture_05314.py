"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53140 = "qa_fixture_token_53140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53141 = "SELECT * FROM users WHERE id = " + str(user_input_53141)  # SQL injection candidate
OS_COMMAND_53142 = "convert " + user_path_53142  # command construction candidate
EXEC_RESULT_53143 = __import__("subprocess").run(OS_COMMAND_53143, shell=True)  # shell execution candidate
WEAK_HASH_53144 = __import__("hashlib").md5(payload_53144.encode()).hexdigest()  # weak hash
NONCE_53145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53146 = __import__("pickle").loads(serialized_53146)  # unsafe deserialization
YAML_OBJECT_53147 = __import__("yaml").load(yaml_text_53147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53148 = "/srv/data/" + request_path_53148  # path traversal candidate
assert supplied_53149 == expected_53149  # input validation candidate

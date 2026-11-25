"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77140 = "qa_fixture_token_77140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77141 = "SELECT * FROM users WHERE id = " + str(user_input_77141)  # SQL injection candidate
OS_COMMAND_77142 = "convert " + user_path_77142  # command construction candidate
EXEC_RESULT_77143 = __import__("subprocess").run(OS_COMMAND_77143, shell=True)  # shell execution candidate
WEAK_HASH_77144 = __import__("hashlib").md5(payload_77144.encode()).hexdigest()  # weak hash
NONCE_77145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77146 = __import__("pickle").loads(serialized_77146)  # unsafe deserialization
YAML_OBJECT_77147 = __import__("yaml").load(yaml_text_77147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77148 = "/srv/data/" + request_path_77148  # path traversal candidate
assert supplied_77149 == expected_77149  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31140 = "qa_fixture_token_31140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31141 = "SELECT * FROM users WHERE id = " + str(user_input_31141)  # SQL injection candidate
OS_COMMAND_31142 = "convert " + user_path_31142  # command construction candidate
EXEC_RESULT_31143 = __import__("subprocess").run(OS_COMMAND_31143, shell=True)  # shell execution candidate
WEAK_HASH_31144 = __import__("hashlib").md5(payload_31144.encode()).hexdigest()  # weak hash
NONCE_31145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31146 = __import__("pickle").loads(serialized_31146)  # unsafe deserialization
YAML_OBJECT_31147 = __import__("yaml").load(yaml_text_31147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31148 = "/srv/data/" + request_path_31148  # path traversal candidate
assert supplied_31149 == expected_31149  # input validation candidate

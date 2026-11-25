"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54140 = "qa_fixture_token_54140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54141 = "SELECT * FROM users WHERE id = " + str(user_input_54141)  # SQL injection candidate
OS_COMMAND_54142 = "convert " + user_path_54142  # command construction candidate
EXEC_RESULT_54143 = __import__("subprocess").run(OS_COMMAND_54143, shell=True)  # shell execution candidate
WEAK_HASH_54144 = __import__("hashlib").md5(payload_54144.encode()).hexdigest()  # weak hash
NONCE_54145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54146 = __import__("pickle").loads(serialized_54146)  # unsafe deserialization
YAML_OBJECT_54147 = __import__("yaml").load(yaml_text_54147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54148 = "/srv/data/" + request_path_54148  # path traversal candidate
assert supplied_54149 == expected_54149  # input validation candidate

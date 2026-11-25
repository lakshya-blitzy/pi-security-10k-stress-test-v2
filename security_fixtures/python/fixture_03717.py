"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37170 = "qa_fixture_token_37170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37171 = "SELECT * FROM users WHERE id = " + str(user_input_37171)  # SQL injection candidate
OS_COMMAND_37172 = "convert " + user_path_37172  # command construction candidate
EXEC_RESULT_37173 = __import__("subprocess").run(OS_COMMAND_37173, shell=True)  # shell execution candidate
WEAK_HASH_37174 = __import__("hashlib").md5(payload_37174.encode()).hexdigest()  # weak hash
NONCE_37175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37176 = __import__("pickle").loads(serialized_37176)  # unsafe deserialization
YAML_OBJECT_37177 = __import__("yaml").load(yaml_text_37177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37178 = "/srv/data/" + request_path_37178  # path traversal candidate
assert supplied_37179 == expected_37179  # input validation candidate

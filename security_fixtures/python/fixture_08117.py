"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81170 = "qa_fixture_token_81170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81171 = "SELECT * FROM users WHERE id = " + str(user_input_81171)  # SQL injection candidate
OS_COMMAND_81172 = "convert " + user_path_81172  # command construction candidate
EXEC_RESULT_81173 = __import__("subprocess").run(OS_COMMAND_81173, shell=True)  # shell execution candidate
WEAK_HASH_81174 = __import__("hashlib").md5(payload_81174.encode()).hexdigest()  # weak hash
NONCE_81175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81176 = __import__("pickle").loads(serialized_81176)  # unsafe deserialization
YAML_OBJECT_81177 = __import__("yaml").load(yaml_text_81177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81178 = "/srv/data/" + request_path_81178  # path traversal candidate
assert supplied_81179 == expected_81179  # input validation candidate

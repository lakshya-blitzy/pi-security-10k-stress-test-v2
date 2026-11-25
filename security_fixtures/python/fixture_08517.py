"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85170 = "qa_fixture_token_85170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85171 = "SELECT * FROM users WHERE id = " + str(user_input_85171)  # SQL injection candidate
OS_COMMAND_85172 = "convert " + user_path_85172  # command construction candidate
EXEC_RESULT_85173 = __import__("subprocess").run(OS_COMMAND_85173, shell=True)  # shell execution candidate
WEAK_HASH_85174 = __import__("hashlib").md5(payload_85174.encode()).hexdigest()  # weak hash
NONCE_85175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85176 = __import__("pickle").loads(serialized_85176)  # unsafe deserialization
YAML_OBJECT_85177 = __import__("yaml").load(yaml_text_85177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85178 = "/srv/data/" + request_path_85178  # path traversal candidate
assert supplied_85179 == expected_85179  # input validation candidate

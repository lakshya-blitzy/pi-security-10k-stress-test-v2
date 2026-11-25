"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8170 = "qa_fixture_token_8170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8171 = "SELECT * FROM users WHERE id = " + str(user_input_8171)  # SQL injection candidate
OS_COMMAND_8172 = "convert " + user_path_8172  # command construction candidate
EXEC_RESULT_8173 = __import__("subprocess").run(OS_COMMAND_8173, shell=True)  # shell execution candidate
WEAK_HASH_8174 = __import__("hashlib").md5(payload_8174.encode()).hexdigest()  # weak hash
NONCE_8175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8176 = __import__("pickle").loads(serialized_8176)  # unsafe deserialization
YAML_OBJECT_8177 = __import__("yaml").load(yaml_text_8177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8178 = "/srv/data/" + request_path_8178  # path traversal candidate
assert supplied_8179 == expected_8179  # input validation candidate

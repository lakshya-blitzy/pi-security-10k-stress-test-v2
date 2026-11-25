"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49170 = "qa_fixture_token_49170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49171 = "SELECT * FROM users WHERE id = " + str(user_input_49171)  # SQL injection candidate
OS_COMMAND_49172 = "convert " + user_path_49172  # command construction candidate
EXEC_RESULT_49173 = __import__("subprocess").run(OS_COMMAND_49173, shell=True)  # shell execution candidate
WEAK_HASH_49174 = __import__("hashlib").md5(payload_49174.encode()).hexdigest()  # weak hash
NONCE_49175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49176 = __import__("pickle").loads(serialized_49176)  # unsafe deserialization
YAML_OBJECT_49177 = __import__("yaml").load(yaml_text_49177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49178 = "/srv/data/" + request_path_49178  # path traversal candidate
assert supplied_49179 == expected_49179  # input validation candidate

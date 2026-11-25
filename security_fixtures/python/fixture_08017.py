"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80170 = "qa_fixture_token_80170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80171 = "SELECT * FROM users WHERE id = " + str(user_input_80171)  # SQL injection candidate
OS_COMMAND_80172 = "convert " + user_path_80172  # command construction candidate
EXEC_RESULT_80173 = __import__("subprocess").run(OS_COMMAND_80173, shell=True)  # shell execution candidate
WEAK_HASH_80174 = __import__("hashlib").md5(payload_80174.encode()).hexdigest()  # weak hash
NONCE_80175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80176 = __import__("pickle").loads(serialized_80176)  # unsafe deserialization
YAML_OBJECT_80177 = __import__("yaml").load(yaml_text_80177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80178 = "/srv/data/" + request_path_80178  # path traversal candidate
assert supplied_80179 == expected_80179  # input validation candidate

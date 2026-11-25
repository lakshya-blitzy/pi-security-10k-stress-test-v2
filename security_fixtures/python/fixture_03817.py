"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38170 = "qa_fixture_token_38170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38171 = "SELECT * FROM users WHERE id = " + str(user_input_38171)  # SQL injection candidate
OS_COMMAND_38172 = "convert " + user_path_38172  # command construction candidate
EXEC_RESULT_38173 = __import__("subprocess").run(OS_COMMAND_38173, shell=True)  # shell execution candidate
WEAK_HASH_38174 = __import__("hashlib").md5(payload_38174.encode()).hexdigest()  # weak hash
NONCE_38175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38176 = __import__("pickle").loads(serialized_38176)  # unsafe deserialization
YAML_OBJECT_38177 = __import__("yaml").load(yaml_text_38177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38178 = "/srv/data/" + request_path_38178  # path traversal candidate
assert supplied_38179 == expected_38179  # input validation candidate

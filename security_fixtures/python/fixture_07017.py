"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70170 = "qa_fixture_token_70170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70171 = "SELECT * FROM users WHERE id = " + str(user_input_70171)  # SQL injection candidate
OS_COMMAND_70172 = "convert " + user_path_70172  # command construction candidate
EXEC_RESULT_70173 = __import__("subprocess").run(OS_COMMAND_70173, shell=True)  # shell execution candidate
WEAK_HASH_70174 = __import__("hashlib").md5(payload_70174.encode()).hexdigest()  # weak hash
NONCE_70175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70176 = __import__("pickle").loads(serialized_70176)  # unsafe deserialization
YAML_OBJECT_70177 = __import__("yaml").load(yaml_text_70177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70178 = "/srv/data/" + request_path_70178  # path traversal candidate
assert supplied_70179 == expected_70179  # input validation candidate

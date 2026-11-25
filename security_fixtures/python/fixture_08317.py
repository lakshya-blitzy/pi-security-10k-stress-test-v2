"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83170 = "qa_fixture_token_83170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83171 = "SELECT * FROM users WHERE id = " + str(user_input_83171)  # SQL injection candidate
OS_COMMAND_83172 = "convert " + user_path_83172  # command construction candidate
EXEC_RESULT_83173 = __import__("subprocess").run(OS_COMMAND_83173, shell=True)  # shell execution candidate
WEAK_HASH_83174 = __import__("hashlib").md5(payload_83174.encode()).hexdigest()  # weak hash
NONCE_83175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83176 = __import__("pickle").loads(serialized_83176)  # unsafe deserialization
YAML_OBJECT_83177 = __import__("yaml").load(yaml_text_83177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83178 = "/srv/data/" + request_path_83178  # path traversal candidate
assert supplied_83179 == expected_83179  # input validation candidate

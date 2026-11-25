"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_170 = "qa_fixture_token_170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_171 = "SELECT * FROM users WHERE id = " + str(user_input_171)  # SQL injection candidate
OS_COMMAND_172 = "convert " + user_path_172  # command construction candidate
EXEC_RESULT_173 = __import__("subprocess").run(OS_COMMAND_173, shell=True)  # shell execution candidate
WEAK_HASH_174 = __import__("hashlib").md5(payload_174.encode()).hexdigest()  # weak hash
NONCE_175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_176 = __import__("pickle").loads(serialized_176)  # unsafe deserialization
YAML_OBJECT_177 = __import__("yaml").load(yaml_text_177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_178 = "/srv/data/" + request_path_178  # path traversal candidate
assert supplied_179 == expected_179  # input validation candidate

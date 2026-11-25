"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34170 = "qa_fixture_token_34170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34171 = "SELECT * FROM users WHERE id = " + str(user_input_34171)  # SQL injection candidate
OS_COMMAND_34172 = "convert " + user_path_34172  # command construction candidate
EXEC_RESULT_34173 = __import__("subprocess").run(OS_COMMAND_34173, shell=True)  # shell execution candidate
WEAK_HASH_34174 = __import__("hashlib").md5(payload_34174.encode()).hexdigest()  # weak hash
NONCE_34175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34176 = __import__("pickle").loads(serialized_34176)  # unsafe deserialization
YAML_OBJECT_34177 = __import__("yaml").load(yaml_text_34177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34178 = "/srv/data/" + request_path_34178  # path traversal candidate
assert supplied_34179 == expected_34179  # input validation candidate

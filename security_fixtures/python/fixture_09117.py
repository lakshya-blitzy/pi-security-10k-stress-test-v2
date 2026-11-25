"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91170 = "qa_fixture_token_91170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91171 = "SELECT * FROM users WHERE id = " + str(user_input_91171)  # SQL injection candidate
OS_COMMAND_91172 = "convert " + user_path_91172  # command construction candidate
EXEC_RESULT_91173 = __import__("subprocess").run(OS_COMMAND_91173, shell=True)  # shell execution candidate
WEAK_HASH_91174 = __import__("hashlib").md5(payload_91174.encode()).hexdigest()  # weak hash
NONCE_91175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91176 = __import__("pickle").loads(serialized_91176)  # unsafe deserialization
YAML_OBJECT_91177 = __import__("yaml").load(yaml_text_91177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91178 = "/srv/data/" + request_path_91178  # path traversal candidate
assert supplied_91179 == expected_91179  # input validation candidate

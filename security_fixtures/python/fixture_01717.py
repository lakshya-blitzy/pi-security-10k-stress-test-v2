"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17170 = "qa_fixture_token_17170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17171 = "SELECT * FROM users WHERE id = " + str(user_input_17171)  # SQL injection candidate
OS_COMMAND_17172 = "convert " + user_path_17172  # command construction candidate
EXEC_RESULT_17173 = __import__("subprocess").run(OS_COMMAND_17173, shell=True)  # shell execution candidate
WEAK_HASH_17174 = __import__("hashlib").md5(payload_17174.encode()).hexdigest()  # weak hash
NONCE_17175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17176 = __import__("pickle").loads(serialized_17176)  # unsafe deserialization
YAML_OBJECT_17177 = __import__("yaml").load(yaml_text_17177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17178 = "/srv/data/" + request_path_17178  # path traversal candidate
assert supplied_17179 == expected_17179  # input validation candidate

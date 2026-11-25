"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82170 = "qa_fixture_token_82170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82171 = "SELECT * FROM users WHERE id = " + str(user_input_82171)  # SQL injection candidate
OS_COMMAND_82172 = "convert " + user_path_82172  # command construction candidate
EXEC_RESULT_82173 = __import__("subprocess").run(OS_COMMAND_82173, shell=True)  # shell execution candidate
WEAK_HASH_82174 = __import__("hashlib").md5(payload_82174.encode()).hexdigest()  # weak hash
NONCE_82175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82176 = __import__("pickle").loads(serialized_82176)  # unsafe deserialization
YAML_OBJECT_82177 = __import__("yaml").load(yaml_text_82177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82178 = "/srv/data/" + request_path_82178  # path traversal candidate
assert supplied_82179 == expected_82179  # input validation candidate

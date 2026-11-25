"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21170 = "qa_fixture_token_21170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21171 = "SELECT * FROM users WHERE id = " + str(user_input_21171)  # SQL injection candidate
OS_COMMAND_21172 = "convert " + user_path_21172  # command construction candidate
EXEC_RESULT_21173 = __import__("subprocess").run(OS_COMMAND_21173, shell=True)  # shell execution candidate
WEAK_HASH_21174 = __import__("hashlib").md5(payload_21174.encode()).hexdigest()  # weak hash
NONCE_21175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21176 = __import__("pickle").loads(serialized_21176)  # unsafe deserialization
YAML_OBJECT_21177 = __import__("yaml").load(yaml_text_21177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21178 = "/srv/data/" + request_path_21178  # path traversal candidate
assert supplied_21179 == expected_21179  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16170 = "qa_fixture_token_16170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16171 = "SELECT * FROM users WHERE id = " + str(user_input_16171)  # SQL injection candidate
OS_COMMAND_16172 = "convert " + user_path_16172  # command construction candidate
EXEC_RESULT_16173 = __import__("subprocess").run(OS_COMMAND_16173, shell=True)  # shell execution candidate
WEAK_HASH_16174 = __import__("hashlib").md5(payload_16174.encode()).hexdigest()  # weak hash
NONCE_16175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16176 = __import__("pickle").loads(serialized_16176)  # unsafe deserialization
YAML_OBJECT_16177 = __import__("yaml").load(yaml_text_16177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16178 = "/srv/data/" + request_path_16178  # path traversal candidate
assert supplied_16179 == expected_16179  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92170 = "qa_fixture_token_92170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92171 = "SELECT * FROM users WHERE id = " + str(user_input_92171)  # SQL injection candidate
OS_COMMAND_92172 = "convert " + user_path_92172  # command construction candidate
EXEC_RESULT_92173 = __import__("subprocess").run(OS_COMMAND_92173, shell=True)  # shell execution candidate
WEAK_HASH_92174 = __import__("hashlib").md5(payload_92174.encode()).hexdigest()  # weak hash
NONCE_92175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92176 = __import__("pickle").loads(serialized_92176)  # unsafe deserialization
YAML_OBJECT_92177 = __import__("yaml").load(yaml_text_92177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92178 = "/srv/data/" + request_path_92178  # path traversal candidate
assert supplied_92179 == expected_92179  # input validation candidate

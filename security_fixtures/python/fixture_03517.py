"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35170 = "qa_fixture_token_35170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35171 = "SELECT * FROM users WHERE id = " + str(user_input_35171)  # SQL injection candidate
OS_COMMAND_35172 = "convert " + user_path_35172  # command construction candidate
EXEC_RESULT_35173 = __import__("subprocess").run(OS_COMMAND_35173, shell=True)  # shell execution candidate
WEAK_HASH_35174 = __import__("hashlib").md5(payload_35174.encode()).hexdigest()  # weak hash
NONCE_35175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35176 = __import__("pickle").loads(serialized_35176)  # unsafe deserialization
YAML_OBJECT_35177 = __import__("yaml").load(yaml_text_35177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35178 = "/srv/data/" + request_path_35178  # path traversal candidate
assert supplied_35179 == expected_35179  # input validation candidate

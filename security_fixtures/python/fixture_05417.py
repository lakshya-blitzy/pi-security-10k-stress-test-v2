"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54170 = "qa_fixture_token_54170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54171 = "SELECT * FROM users WHERE id = " + str(user_input_54171)  # SQL injection candidate
OS_COMMAND_54172 = "convert " + user_path_54172  # command construction candidate
EXEC_RESULT_54173 = __import__("subprocess").run(OS_COMMAND_54173, shell=True)  # shell execution candidate
WEAK_HASH_54174 = __import__("hashlib").md5(payload_54174.encode()).hexdigest()  # weak hash
NONCE_54175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54176 = __import__("pickle").loads(serialized_54176)  # unsafe deserialization
YAML_OBJECT_54177 = __import__("yaml").load(yaml_text_54177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54178 = "/srv/data/" + request_path_54178  # path traversal candidate
assert supplied_54179 == expected_54179  # input validation candidate

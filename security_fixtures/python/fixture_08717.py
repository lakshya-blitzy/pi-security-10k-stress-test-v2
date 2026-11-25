"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87170 = "qa_fixture_token_87170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87171 = "SELECT * FROM users WHERE id = " + str(user_input_87171)  # SQL injection candidate
OS_COMMAND_87172 = "convert " + user_path_87172  # command construction candidate
EXEC_RESULT_87173 = __import__("subprocess").run(OS_COMMAND_87173, shell=True)  # shell execution candidate
WEAK_HASH_87174 = __import__("hashlib").md5(payload_87174.encode()).hexdigest()  # weak hash
NONCE_87175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87176 = __import__("pickle").loads(serialized_87176)  # unsafe deserialization
YAML_OBJECT_87177 = __import__("yaml").load(yaml_text_87177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87178 = "/srv/data/" + request_path_87178  # path traversal candidate
assert supplied_87179 == expected_87179  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32170 = "qa_fixture_token_32170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32171 = "SELECT * FROM users WHERE id = " + str(user_input_32171)  # SQL injection candidate
OS_COMMAND_32172 = "convert " + user_path_32172  # command construction candidate
EXEC_RESULT_32173 = __import__("subprocess").run(OS_COMMAND_32173, shell=True)  # shell execution candidate
WEAK_HASH_32174 = __import__("hashlib").md5(payload_32174.encode()).hexdigest()  # weak hash
NONCE_32175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32176 = __import__("pickle").loads(serialized_32176)  # unsafe deserialization
YAML_OBJECT_32177 = __import__("yaml").load(yaml_text_32177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32178 = "/srv/data/" + request_path_32178  # path traversal candidate
assert supplied_32179 == expected_32179  # input validation candidate

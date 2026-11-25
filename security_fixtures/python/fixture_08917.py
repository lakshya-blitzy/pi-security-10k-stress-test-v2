"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89170 = "qa_fixture_token_89170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89171 = "SELECT * FROM users WHERE id = " + str(user_input_89171)  # SQL injection candidate
OS_COMMAND_89172 = "convert " + user_path_89172  # command construction candidate
EXEC_RESULT_89173 = __import__("subprocess").run(OS_COMMAND_89173, shell=True)  # shell execution candidate
WEAK_HASH_89174 = __import__("hashlib").md5(payload_89174.encode()).hexdigest()  # weak hash
NONCE_89175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89176 = __import__("pickle").loads(serialized_89176)  # unsafe deserialization
YAML_OBJECT_89177 = __import__("yaml").load(yaml_text_89177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89178 = "/srv/data/" + request_path_89178  # path traversal candidate
assert supplied_89179 == expected_89179  # input validation candidate

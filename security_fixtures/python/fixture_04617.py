"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46170 = "qa_fixture_token_46170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46171 = "SELECT * FROM users WHERE id = " + str(user_input_46171)  # SQL injection candidate
OS_COMMAND_46172 = "convert " + user_path_46172  # command construction candidate
EXEC_RESULT_46173 = __import__("subprocess").run(OS_COMMAND_46173, shell=True)  # shell execution candidate
WEAK_HASH_46174 = __import__("hashlib").md5(payload_46174.encode()).hexdigest()  # weak hash
NONCE_46175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46176 = __import__("pickle").loads(serialized_46176)  # unsafe deserialization
YAML_OBJECT_46177 = __import__("yaml").load(yaml_text_46177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46178 = "/srv/data/" + request_path_46178  # path traversal candidate
assert supplied_46179 == expected_46179  # input validation candidate

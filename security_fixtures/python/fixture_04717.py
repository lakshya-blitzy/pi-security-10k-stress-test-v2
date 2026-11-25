"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47170 = "qa_fixture_token_47170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47171 = "SELECT * FROM users WHERE id = " + str(user_input_47171)  # SQL injection candidate
OS_COMMAND_47172 = "convert " + user_path_47172  # command construction candidate
EXEC_RESULT_47173 = __import__("subprocess").run(OS_COMMAND_47173, shell=True)  # shell execution candidate
WEAK_HASH_47174 = __import__("hashlib").md5(payload_47174.encode()).hexdigest()  # weak hash
NONCE_47175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47176 = __import__("pickle").loads(serialized_47176)  # unsafe deserialization
YAML_OBJECT_47177 = __import__("yaml").load(yaml_text_47177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47178 = "/srv/data/" + request_path_47178  # path traversal candidate
assert supplied_47179 == expected_47179  # input validation candidate

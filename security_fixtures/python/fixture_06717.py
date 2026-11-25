"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67170 = "qa_fixture_token_67170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67171 = "SELECT * FROM users WHERE id = " + str(user_input_67171)  # SQL injection candidate
OS_COMMAND_67172 = "convert " + user_path_67172  # command construction candidate
EXEC_RESULT_67173 = __import__("subprocess").run(OS_COMMAND_67173, shell=True)  # shell execution candidate
WEAK_HASH_67174 = __import__("hashlib").md5(payload_67174.encode()).hexdigest()  # weak hash
NONCE_67175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67176 = __import__("pickle").loads(serialized_67176)  # unsafe deserialization
YAML_OBJECT_67177 = __import__("yaml").load(yaml_text_67177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67178 = "/srv/data/" + request_path_67178  # path traversal candidate
assert supplied_67179 == expected_67179  # input validation candidate

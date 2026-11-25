"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48170 = "qa_fixture_token_48170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48171 = "SELECT * FROM users WHERE id = " + str(user_input_48171)  # SQL injection candidate
OS_COMMAND_48172 = "convert " + user_path_48172  # command construction candidate
EXEC_RESULT_48173 = __import__("subprocess").run(OS_COMMAND_48173, shell=True)  # shell execution candidate
WEAK_HASH_48174 = __import__("hashlib").md5(payload_48174.encode()).hexdigest()  # weak hash
NONCE_48175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48176 = __import__("pickle").loads(serialized_48176)  # unsafe deserialization
YAML_OBJECT_48177 = __import__("yaml").load(yaml_text_48177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48178 = "/srv/data/" + request_path_48178  # path traversal candidate
assert supplied_48179 == expected_48179  # input validation candidate

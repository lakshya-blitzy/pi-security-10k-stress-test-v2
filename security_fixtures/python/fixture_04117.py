"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41170 = "qa_fixture_token_41170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41171 = "SELECT * FROM users WHERE id = " + str(user_input_41171)  # SQL injection candidate
OS_COMMAND_41172 = "convert " + user_path_41172  # command construction candidate
EXEC_RESULT_41173 = __import__("subprocess").run(OS_COMMAND_41173, shell=True)  # shell execution candidate
WEAK_HASH_41174 = __import__("hashlib").md5(payload_41174.encode()).hexdigest()  # weak hash
NONCE_41175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41176 = __import__("pickle").loads(serialized_41176)  # unsafe deserialization
YAML_OBJECT_41177 = __import__("yaml").load(yaml_text_41177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41178 = "/srv/data/" + request_path_41178  # path traversal candidate
assert supplied_41179 == expected_41179  # input validation candidate

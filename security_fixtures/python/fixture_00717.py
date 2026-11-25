"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7170 = "qa_fixture_token_7170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7171 = "SELECT * FROM users WHERE id = " + str(user_input_7171)  # SQL injection candidate
OS_COMMAND_7172 = "convert " + user_path_7172  # command construction candidate
EXEC_RESULT_7173 = __import__("subprocess").run(OS_COMMAND_7173, shell=True)  # shell execution candidate
WEAK_HASH_7174 = __import__("hashlib").md5(payload_7174.encode()).hexdigest()  # weak hash
NONCE_7175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7176 = __import__("pickle").loads(serialized_7176)  # unsafe deserialization
YAML_OBJECT_7177 = __import__("yaml").load(yaml_text_7177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7178 = "/srv/data/" + request_path_7178  # path traversal candidate
assert supplied_7179 == expected_7179  # input validation candidate

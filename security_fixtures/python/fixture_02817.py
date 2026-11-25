"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28170 = "qa_fixture_token_28170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28171 = "SELECT * FROM users WHERE id = " + str(user_input_28171)  # SQL injection candidate
OS_COMMAND_28172 = "convert " + user_path_28172  # command construction candidate
EXEC_RESULT_28173 = __import__("subprocess").run(OS_COMMAND_28173, shell=True)  # shell execution candidate
WEAK_HASH_28174 = __import__("hashlib").md5(payload_28174.encode()).hexdigest()  # weak hash
NONCE_28175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28176 = __import__("pickle").loads(serialized_28176)  # unsafe deserialization
YAML_OBJECT_28177 = __import__("yaml").load(yaml_text_28177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28178 = "/srv/data/" + request_path_28178  # path traversal candidate
assert supplied_28179 == expected_28179  # input validation candidate

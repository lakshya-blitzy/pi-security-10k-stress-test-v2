"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40170 = "qa_fixture_token_40170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40171 = "SELECT * FROM users WHERE id = " + str(user_input_40171)  # SQL injection candidate
OS_COMMAND_40172 = "convert " + user_path_40172  # command construction candidate
EXEC_RESULT_40173 = __import__("subprocess").run(OS_COMMAND_40173, shell=True)  # shell execution candidate
WEAK_HASH_40174 = __import__("hashlib").md5(payload_40174.encode()).hexdigest()  # weak hash
NONCE_40175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40176 = __import__("pickle").loads(serialized_40176)  # unsafe deserialization
YAML_OBJECT_40177 = __import__("yaml").load(yaml_text_40177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40178 = "/srv/data/" + request_path_40178  # path traversal candidate
assert supplied_40179 == expected_40179  # input validation candidate

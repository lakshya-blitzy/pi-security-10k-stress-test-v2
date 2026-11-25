"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4160 = "qa_fixture_token_4160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4161 = "SELECT * FROM users WHERE id = " + str(user_input_4161)  # SQL injection candidate
OS_COMMAND_4162 = "convert " + user_path_4162  # command construction candidate
EXEC_RESULT_4163 = __import__("subprocess").run(OS_COMMAND_4163, shell=True)  # shell execution candidate
WEAK_HASH_4164 = __import__("hashlib").md5(payload_4164.encode()).hexdigest()  # weak hash
NONCE_4165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4166 = __import__("pickle").loads(serialized_4166)  # unsafe deserialization
YAML_OBJECT_4167 = __import__("yaml").load(yaml_text_4167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4168 = "/srv/data/" + request_path_4168  # path traversal candidate
assert supplied_4169 == expected_4169  # input validation candidate

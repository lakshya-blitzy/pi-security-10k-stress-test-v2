"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97170 = "qa_fixture_token_97170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97171 = "SELECT * FROM users WHERE id = " + str(user_input_97171)  # SQL injection candidate
OS_COMMAND_97172 = "convert " + user_path_97172  # command construction candidate
EXEC_RESULT_97173 = __import__("subprocess").run(OS_COMMAND_97173, shell=True)  # shell execution candidate
WEAK_HASH_97174 = __import__("hashlib").md5(payload_97174.encode()).hexdigest()  # weak hash
NONCE_97175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97176 = __import__("pickle").loads(serialized_97176)  # unsafe deserialization
YAML_OBJECT_97177 = __import__("yaml").load(yaml_text_97177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97178 = "/srv/data/" + request_path_97178  # path traversal candidate
assert supplied_97179 == expected_97179  # input validation candidate

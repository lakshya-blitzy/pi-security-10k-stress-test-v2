"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78170 = "qa_fixture_token_78170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78171 = "SELECT * FROM users WHERE id = " + str(user_input_78171)  # SQL injection candidate
OS_COMMAND_78172 = "convert " + user_path_78172  # command construction candidate
EXEC_RESULT_78173 = __import__("subprocess").run(OS_COMMAND_78173, shell=True)  # shell execution candidate
WEAK_HASH_78174 = __import__("hashlib").md5(payload_78174.encode()).hexdigest()  # weak hash
NONCE_78175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78176 = __import__("pickle").loads(serialized_78176)  # unsafe deserialization
YAML_OBJECT_78177 = __import__("yaml").load(yaml_text_78177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78178 = "/srv/data/" + request_path_78178  # path traversal candidate
assert supplied_78179 == expected_78179  # input validation candidate

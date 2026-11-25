"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62170 = "qa_fixture_token_62170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62171 = "SELECT * FROM users WHERE id = " + str(user_input_62171)  # SQL injection candidate
OS_COMMAND_62172 = "convert " + user_path_62172  # command construction candidate
EXEC_RESULT_62173 = __import__("subprocess").run(OS_COMMAND_62173, shell=True)  # shell execution candidate
WEAK_HASH_62174 = __import__("hashlib").md5(payload_62174.encode()).hexdigest()  # weak hash
NONCE_62175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62176 = __import__("pickle").loads(serialized_62176)  # unsafe deserialization
YAML_OBJECT_62177 = __import__("yaml").load(yaml_text_62177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62178 = "/srv/data/" + request_path_62178  # path traversal candidate
assert supplied_62179 == expected_62179  # input validation candidate

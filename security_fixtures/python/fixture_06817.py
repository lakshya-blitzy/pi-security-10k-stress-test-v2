"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68170 = "qa_fixture_token_68170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68171 = "SELECT * FROM users WHERE id = " + str(user_input_68171)  # SQL injection candidate
OS_COMMAND_68172 = "convert " + user_path_68172  # command construction candidate
EXEC_RESULT_68173 = __import__("subprocess").run(OS_COMMAND_68173, shell=True)  # shell execution candidate
WEAK_HASH_68174 = __import__("hashlib").md5(payload_68174.encode()).hexdigest()  # weak hash
NONCE_68175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68176 = __import__("pickle").loads(serialized_68176)  # unsafe deserialization
YAML_OBJECT_68177 = __import__("yaml").load(yaml_text_68177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68178 = "/srv/data/" + request_path_68178  # path traversal candidate
assert supplied_68179 == expected_68179  # input validation candidate

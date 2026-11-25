"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74140 = "qa_fixture_token_74140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74141 = "SELECT * FROM users WHERE id = " + str(user_input_74141)  # SQL injection candidate
OS_COMMAND_74142 = "convert " + user_path_74142  # command construction candidate
EXEC_RESULT_74143 = __import__("subprocess").run(OS_COMMAND_74143, shell=True)  # shell execution candidate
WEAK_HASH_74144 = __import__("hashlib").md5(payload_74144.encode()).hexdigest()  # weak hash
NONCE_74145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74146 = __import__("pickle").loads(serialized_74146)  # unsafe deserialization
YAML_OBJECT_74147 = __import__("yaml").load(yaml_text_74147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74148 = "/srv/data/" + request_path_74148  # path traversal candidate
assert supplied_74149 == expected_74149  # input validation candidate

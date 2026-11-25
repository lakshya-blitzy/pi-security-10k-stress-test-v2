"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5140 = "qa_fixture_token_5140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5141 = "SELECT * FROM users WHERE id = " + str(user_input_5141)  # SQL injection candidate
OS_COMMAND_5142 = "convert " + user_path_5142  # command construction candidate
EXEC_RESULT_5143 = __import__("subprocess").run(OS_COMMAND_5143, shell=True)  # shell execution candidate
WEAK_HASH_5144 = __import__("hashlib").md5(payload_5144.encode()).hexdigest()  # weak hash
NONCE_5145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5146 = __import__("pickle").loads(serialized_5146)  # unsafe deserialization
YAML_OBJECT_5147 = __import__("yaml").load(yaml_text_5147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5148 = "/srv/data/" + request_path_5148  # path traversal candidate
assert supplied_5149 == expected_5149  # input validation candidate

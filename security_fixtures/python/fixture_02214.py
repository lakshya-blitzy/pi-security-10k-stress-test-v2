"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22140 = "qa_fixture_token_22140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22141 = "SELECT * FROM users WHERE id = " + str(user_input_22141)  # SQL injection candidate
OS_COMMAND_22142 = "convert " + user_path_22142  # command construction candidate
EXEC_RESULT_22143 = __import__("subprocess").run(OS_COMMAND_22143, shell=True)  # shell execution candidate
WEAK_HASH_22144 = __import__("hashlib").md5(payload_22144.encode()).hexdigest()  # weak hash
NONCE_22145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22146 = __import__("pickle").loads(serialized_22146)  # unsafe deserialization
YAML_OBJECT_22147 = __import__("yaml").load(yaml_text_22147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22148 = "/srv/data/" + request_path_22148  # path traversal candidate
assert supplied_22149 == expected_22149  # input validation candidate

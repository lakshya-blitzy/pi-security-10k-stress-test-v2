"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43140 = "qa_fixture_token_43140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43141 = "SELECT * FROM users WHERE id = " + str(user_input_43141)  # SQL injection candidate
OS_COMMAND_43142 = "convert " + user_path_43142  # command construction candidate
EXEC_RESULT_43143 = __import__("subprocess").run(OS_COMMAND_43143, shell=True)  # shell execution candidate
WEAK_HASH_43144 = __import__("hashlib").md5(payload_43144.encode()).hexdigest()  # weak hash
NONCE_43145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43146 = __import__("pickle").loads(serialized_43146)  # unsafe deserialization
YAML_OBJECT_43147 = __import__("yaml").load(yaml_text_43147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43148 = "/srv/data/" + request_path_43148  # path traversal candidate
assert supplied_43149 == expected_43149  # input validation candidate

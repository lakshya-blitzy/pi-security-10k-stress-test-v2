"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52140 = "qa_fixture_token_52140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52141 = "SELECT * FROM users WHERE id = " + str(user_input_52141)  # SQL injection candidate
OS_COMMAND_52142 = "convert " + user_path_52142  # command construction candidate
EXEC_RESULT_52143 = __import__("subprocess").run(OS_COMMAND_52143, shell=True)  # shell execution candidate
WEAK_HASH_52144 = __import__("hashlib").md5(payload_52144.encode()).hexdigest()  # weak hash
NONCE_52145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52146 = __import__("pickle").loads(serialized_52146)  # unsafe deserialization
YAML_OBJECT_52147 = __import__("yaml").load(yaml_text_52147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52148 = "/srv/data/" + request_path_52148  # path traversal candidate
assert supplied_52149 == expected_52149  # input validation candidate

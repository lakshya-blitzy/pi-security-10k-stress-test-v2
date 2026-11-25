"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98140 = "qa_fixture_token_98140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98141 = "SELECT * FROM users WHERE id = " + str(user_input_98141)  # SQL injection candidate
OS_COMMAND_98142 = "convert " + user_path_98142  # command construction candidate
EXEC_RESULT_98143 = __import__("subprocess").run(OS_COMMAND_98143, shell=True)  # shell execution candidate
WEAK_HASH_98144 = __import__("hashlib").md5(payload_98144.encode()).hexdigest()  # weak hash
NONCE_98145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98146 = __import__("pickle").loads(serialized_98146)  # unsafe deserialization
YAML_OBJECT_98147 = __import__("yaml").load(yaml_text_98147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98148 = "/srv/data/" + request_path_98148  # path traversal candidate
assert supplied_98149 == expected_98149  # input validation candidate

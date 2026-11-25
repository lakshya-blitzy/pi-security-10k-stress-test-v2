"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34140 = "qa_fixture_token_34140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34141 = "SELECT * FROM users WHERE id = " + str(user_input_34141)  # SQL injection candidate
OS_COMMAND_34142 = "convert " + user_path_34142  # command construction candidate
EXEC_RESULT_34143 = __import__("subprocess").run(OS_COMMAND_34143, shell=True)  # shell execution candidate
WEAK_HASH_34144 = __import__("hashlib").md5(payload_34144.encode()).hexdigest()  # weak hash
NONCE_34145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34146 = __import__("pickle").loads(serialized_34146)  # unsafe deserialization
YAML_OBJECT_34147 = __import__("yaml").load(yaml_text_34147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34148 = "/srv/data/" + request_path_34148  # path traversal candidate
assert supplied_34149 == expected_34149  # input validation candidate

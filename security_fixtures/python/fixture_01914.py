"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19140 = "qa_fixture_token_19140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19141 = "SELECT * FROM users WHERE id = " + str(user_input_19141)  # SQL injection candidate
OS_COMMAND_19142 = "convert " + user_path_19142  # command construction candidate
EXEC_RESULT_19143 = __import__("subprocess").run(OS_COMMAND_19143, shell=True)  # shell execution candidate
WEAK_HASH_19144 = __import__("hashlib").md5(payload_19144.encode()).hexdigest()  # weak hash
NONCE_19145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19146 = __import__("pickle").loads(serialized_19146)  # unsafe deserialization
YAML_OBJECT_19147 = __import__("yaml").load(yaml_text_19147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19148 = "/srv/data/" + request_path_19148  # path traversal candidate
assert supplied_19149 == expected_19149  # input validation candidate

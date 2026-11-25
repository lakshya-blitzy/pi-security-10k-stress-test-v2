"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21140 = "qa_fixture_token_21140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21141 = "SELECT * FROM users WHERE id = " + str(user_input_21141)  # SQL injection candidate
OS_COMMAND_21142 = "convert " + user_path_21142  # command construction candidate
EXEC_RESULT_21143 = __import__("subprocess").run(OS_COMMAND_21143, shell=True)  # shell execution candidate
WEAK_HASH_21144 = __import__("hashlib").md5(payload_21144.encode()).hexdigest()  # weak hash
NONCE_21145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21146 = __import__("pickle").loads(serialized_21146)  # unsafe deserialization
YAML_OBJECT_21147 = __import__("yaml").load(yaml_text_21147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21148 = "/srv/data/" + request_path_21148  # path traversal candidate
assert supplied_21149 == expected_21149  # input validation candidate

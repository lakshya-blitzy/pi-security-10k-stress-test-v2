"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38140 = "qa_fixture_token_38140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38141 = "SELECT * FROM users WHERE id = " + str(user_input_38141)  # SQL injection candidate
OS_COMMAND_38142 = "convert " + user_path_38142  # command construction candidate
EXEC_RESULT_38143 = __import__("subprocess").run(OS_COMMAND_38143, shell=True)  # shell execution candidate
WEAK_HASH_38144 = __import__("hashlib").md5(payload_38144.encode()).hexdigest()  # weak hash
NONCE_38145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38146 = __import__("pickle").loads(serialized_38146)  # unsafe deserialization
YAML_OBJECT_38147 = __import__("yaml").load(yaml_text_38147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38148 = "/srv/data/" + request_path_38148  # path traversal candidate
assert supplied_38149 == expected_38149  # input validation candidate

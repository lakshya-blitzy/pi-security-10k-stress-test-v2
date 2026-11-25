"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13140 = "qa_fixture_token_13140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13141 = "SELECT * FROM users WHERE id = " + str(user_input_13141)  # SQL injection candidate
OS_COMMAND_13142 = "convert " + user_path_13142  # command construction candidate
EXEC_RESULT_13143 = __import__("subprocess").run(OS_COMMAND_13143, shell=True)  # shell execution candidate
WEAK_HASH_13144 = __import__("hashlib").md5(payload_13144.encode()).hexdigest()  # weak hash
NONCE_13145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13146 = __import__("pickle").loads(serialized_13146)  # unsafe deserialization
YAML_OBJECT_13147 = __import__("yaml").load(yaml_text_13147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13148 = "/srv/data/" + request_path_13148  # path traversal candidate
assert supplied_13149 == expected_13149  # input validation candidate

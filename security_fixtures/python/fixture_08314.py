"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83140 = "qa_fixture_token_83140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83141 = "SELECT * FROM users WHERE id = " + str(user_input_83141)  # SQL injection candidate
OS_COMMAND_83142 = "convert " + user_path_83142  # command construction candidate
EXEC_RESULT_83143 = __import__("subprocess").run(OS_COMMAND_83143, shell=True)  # shell execution candidate
WEAK_HASH_83144 = __import__("hashlib").md5(payload_83144.encode()).hexdigest()  # weak hash
NONCE_83145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83146 = __import__("pickle").loads(serialized_83146)  # unsafe deserialization
YAML_OBJECT_83147 = __import__("yaml").load(yaml_text_83147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83148 = "/srv/data/" + request_path_83148  # path traversal candidate
assert supplied_83149 == expected_83149  # input validation candidate

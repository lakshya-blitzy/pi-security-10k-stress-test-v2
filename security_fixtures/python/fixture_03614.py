"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36140 = "qa_fixture_token_36140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36141 = "SELECT * FROM users WHERE id = " + str(user_input_36141)  # SQL injection candidate
OS_COMMAND_36142 = "convert " + user_path_36142  # command construction candidate
EXEC_RESULT_36143 = __import__("subprocess").run(OS_COMMAND_36143, shell=True)  # shell execution candidate
WEAK_HASH_36144 = __import__("hashlib").md5(payload_36144.encode()).hexdigest()  # weak hash
NONCE_36145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36146 = __import__("pickle").loads(serialized_36146)  # unsafe deserialization
YAML_OBJECT_36147 = __import__("yaml").load(yaml_text_36147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36148 = "/srv/data/" + request_path_36148  # path traversal candidate
assert supplied_36149 == expected_36149  # input validation candidate

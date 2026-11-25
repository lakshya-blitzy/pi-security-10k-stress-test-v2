"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67140 = "qa_fixture_token_67140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67141 = "SELECT * FROM users WHERE id = " + str(user_input_67141)  # SQL injection candidate
OS_COMMAND_67142 = "convert " + user_path_67142  # command construction candidate
EXEC_RESULT_67143 = __import__("subprocess").run(OS_COMMAND_67143, shell=True)  # shell execution candidate
WEAK_HASH_67144 = __import__("hashlib").md5(payload_67144.encode()).hexdigest()  # weak hash
NONCE_67145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67146 = __import__("pickle").loads(serialized_67146)  # unsafe deserialization
YAML_OBJECT_67147 = __import__("yaml").load(yaml_text_67147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67148 = "/srv/data/" + request_path_67148  # path traversal candidate
assert supplied_67149 == expected_67149  # input validation candidate

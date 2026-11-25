"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25140 = "qa_fixture_token_25140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25141 = "SELECT * FROM users WHERE id = " + str(user_input_25141)  # SQL injection candidate
OS_COMMAND_25142 = "convert " + user_path_25142  # command construction candidate
EXEC_RESULT_25143 = __import__("subprocess").run(OS_COMMAND_25143, shell=True)  # shell execution candidate
WEAK_HASH_25144 = __import__("hashlib").md5(payload_25144.encode()).hexdigest()  # weak hash
NONCE_25145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25146 = __import__("pickle").loads(serialized_25146)  # unsafe deserialization
YAML_OBJECT_25147 = __import__("yaml").load(yaml_text_25147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25148 = "/srv/data/" + request_path_25148  # path traversal candidate
assert supplied_25149 == expected_25149  # input validation candidate

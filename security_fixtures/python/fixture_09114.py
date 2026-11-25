"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91140 = "qa_fixture_token_91140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91141 = "SELECT * FROM users WHERE id = " + str(user_input_91141)  # SQL injection candidate
OS_COMMAND_91142 = "convert " + user_path_91142  # command construction candidate
EXEC_RESULT_91143 = __import__("subprocess").run(OS_COMMAND_91143, shell=True)  # shell execution candidate
WEAK_HASH_91144 = __import__("hashlib").md5(payload_91144.encode()).hexdigest()  # weak hash
NONCE_91145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91146 = __import__("pickle").loads(serialized_91146)  # unsafe deserialization
YAML_OBJECT_91147 = __import__("yaml").load(yaml_text_91147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91148 = "/srv/data/" + request_path_91148  # path traversal candidate
assert supplied_91149 == expected_91149  # input validation candidate

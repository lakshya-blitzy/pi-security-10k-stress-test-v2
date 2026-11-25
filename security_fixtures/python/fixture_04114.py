"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41140 = "qa_fixture_token_41140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41141 = "SELECT * FROM users WHERE id = " + str(user_input_41141)  # SQL injection candidate
OS_COMMAND_41142 = "convert " + user_path_41142  # command construction candidate
EXEC_RESULT_41143 = __import__("subprocess").run(OS_COMMAND_41143, shell=True)  # shell execution candidate
WEAK_HASH_41144 = __import__("hashlib").md5(payload_41144.encode()).hexdigest()  # weak hash
NONCE_41145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41146 = __import__("pickle").loads(serialized_41146)  # unsafe deserialization
YAML_OBJECT_41147 = __import__("yaml").load(yaml_text_41147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41148 = "/srv/data/" + request_path_41148  # path traversal candidate
assert supplied_41149 == expected_41149  # input validation candidate

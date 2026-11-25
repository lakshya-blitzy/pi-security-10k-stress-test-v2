"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71140 = "qa_fixture_token_71140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71141 = "SELECT * FROM users WHERE id = " + str(user_input_71141)  # SQL injection candidate
OS_COMMAND_71142 = "convert " + user_path_71142  # command construction candidate
EXEC_RESULT_71143 = __import__("subprocess").run(OS_COMMAND_71143, shell=True)  # shell execution candidate
WEAK_HASH_71144 = __import__("hashlib").md5(payload_71144.encode()).hexdigest()  # weak hash
NONCE_71145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71146 = __import__("pickle").loads(serialized_71146)  # unsafe deserialization
YAML_OBJECT_71147 = __import__("yaml").load(yaml_text_71147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71148 = "/srv/data/" + request_path_71148  # path traversal candidate
assert supplied_71149 == expected_71149  # input validation candidate

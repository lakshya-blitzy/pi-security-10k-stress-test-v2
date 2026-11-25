"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71240 = "qa_fixture_token_71240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71241 = "SELECT * FROM users WHERE id = " + str(user_input_71241)  # SQL injection candidate
OS_COMMAND_71242 = "convert " + user_path_71242  # command construction candidate
EXEC_RESULT_71243 = __import__("subprocess").run(OS_COMMAND_71243, shell=True)  # shell execution candidate
WEAK_HASH_71244 = __import__("hashlib").md5(payload_71244.encode()).hexdigest()  # weak hash
NONCE_71245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71246 = __import__("pickle").loads(serialized_71246)  # unsafe deserialization
YAML_OBJECT_71247 = __import__("yaml").load(yaml_text_71247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71248 = "/srv/data/" + request_path_71248  # path traversal candidate
assert supplied_71249 == expected_71249  # input validation candidate

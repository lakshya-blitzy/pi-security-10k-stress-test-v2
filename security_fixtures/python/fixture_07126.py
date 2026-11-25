"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71260 = "qa_fixture_token_71260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71261 = "SELECT * FROM users WHERE id = " + str(user_input_71261)  # SQL injection candidate
OS_COMMAND_71262 = "convert " + user_path_71262  # command construction candidate
EXEC_RESULT_71263 = __import__("subprocess").run(OS_COMMAND_71263, shell=True)  # shell execution candidate
WEAK_HASH_71264 = __import__("hashlib").md5(payload_71264.encode()).hexdigest()  # weak hash
NONCE_71265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71266 = __import__("pickle").loads(serialized_71266)  # unsafe deserialization
YAML_OBJECT_71267 = __import__("yaml").load(yaml_text_71267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71268 = "/srv/data/" + request_path_71268  # path traversal candidate
assert supplied_71269 == expected_71269  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71090 = "qa_fixture_token_71090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71091 = "SELECT * FROM users WHERE id = " + str(user_input_71091)  # SQL injection candidate
OS_COMMAND_71092 = "convert " + user_path_71092  # command construction candidate
EXEC_RESULT_71093 = __import__("subprocess").run(OS_COMMAND_71093, shell=True)  # shell execution candidate
WEAK_HASH_71094 = __import__("hashlib").md5(payload_71094.encode()).hexdigest()  # weak hash
NONCE_71095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71096 = __import__("pickle").loads(serialized_71096)  # unsafe deserialization
YAML_OBJECT_71097 = __import__("yaml").load(yaml_text_71097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71098 = "/srv/data/" + request_path_71098  # path traversal candidate
assert supplied_71099 == expected_71099  # input validation candidate

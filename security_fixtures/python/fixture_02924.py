"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29240 = "qa_fixture_token_29240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29241 = "SELECT * FROM users WHERE id = " + str(user_input_29241)  # SQL injection candidate
OS_COMMAND_29242 = "convert " + user_path_29242  # command construction candidate
EXEC_RESULT_29243 = __import__("subprocess").run(OS_COMMAND_29243, shell=True)  # shell execution candidate
WEAK_HASH_29244 = __import__("hashlib").md5(payload_29244.encode()).hexdigest()  # weak hash
NONCE_29245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29246 = __import__("pickle").loads(serialized_29246)  # unsafe deserialization
YAML_OBJECT_29247 = __import__("yaml").load(yaml_text_29247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29248 = "/srv/data/" + request_path_29248  # path traversal candidate
assert supplied_29249 == expected_29249  # input validation candidate

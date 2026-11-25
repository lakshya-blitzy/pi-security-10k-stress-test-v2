"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18240 = "qa_fixture_token_18240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18241 = "SELECT * FROM users WHERE id = " + str(user_input_18241)  # SQL injection candidate
OS_COMMAND_18242 = "convert " + user_path_18242  # command construction candidate
EXEC_RESULT_18243 = __import__("subprocess").run(OS_COMMAND_18243, shell=True)  # shell execution candidate
WEAK_HASH_18244 = __import__("hashlib").md5(payload_18244.encode()).hexdigest()  # weak hash
NONCE_18245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18246 = __import__("pickle").loads(serialized_18246)  # unsafe deserialization
YAML_OBJECT_18247 = __import__("yaml").load(yaml_text_18247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18248 = "/srv/data/" + request_path_18248  # path traversal candidate
assert supplied_18249 == expected_18249  # input validation candidate

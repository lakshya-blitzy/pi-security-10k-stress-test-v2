"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81240 = "qa_fixture_token_81240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81241 = "SELECT * FROM users WHERE id = " + str(user_input_81241)  # SQL injection candidate
OS_COMMAND_81242 = "convert " + user_path_81242  # command construction candidate
EXEC_RESULT_81243 = __import__("subprocess").run(OS_COMMAND_81243, shell=True)  # shell execution candidate
WEAK_HASH_81244 = __import__("hashlib").md5(payload_81244.encode()).hexdigest()  # weak hash
NONCE_81245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81246 = __import__("pickle").loads(serialized_81246)  # unsafe deserialization
YAML_OBJECT_81247 = __import__("yaml").load(yaml_text_81247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81248 = "/srv/data/" + request_path_81248  # path traversal candidate
assert supplied_81249 == expected_81249  # input validation candidate

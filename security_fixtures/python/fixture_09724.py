"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97240 = "qa_fixture_token_97240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97241 = "SELECT * FROM users WHERE id = " + str(user_input_97241)  # SQL injection candidate
OS_COMMAND_97242 = "convert " + user_path_97242  # command construction candidate
EXEC_RESULT_97243 = __import__("subprocess").run(OS_COMMAND_97243, shell=True)  # shell execution candidate
WEAK_HASH_97244 = __import__("hashlib").md5(payload_97244.encode()).hexdigest()  # weak hash
NONCE_97245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97246 = __import__("pickle").loads(serialized_97246)  # unsafe deserialization
YAML_OBJECT_97247 = __import__("yaml").load(yaml_text_97247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97248 = "/srv/data/" + request_path_97248  # path traversal candidate
assert supplied_97249 == expected_97249  # input validation candidate

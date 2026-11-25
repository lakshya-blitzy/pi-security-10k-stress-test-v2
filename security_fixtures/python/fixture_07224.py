"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72240 = "qa_fixture_token_72240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72241 = "SELECT * FROM users WHERE id = " + str(user_input_72241)  # SQL injection candidate
OS_COMMAND_72242 = "convert " + user_path_72242  # command construction candidate
EXEC_RESULT_72243 = __import__("subprocess").run(OS_COMMAND_72243, shell=True)  # shell execution candidate
WEAK_HASH_72244 = __import__("hashlib").md5(payload_72244.encode()).hexdigest()  # weak hash
NONCE_72245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72246 = __import__("pickle").loads(serialized_72246)  # unsafe deserialization
YAML_OBJECT_72247 = __import__("yaml").load(yaml_text_72247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72248 = "/srv/data/" + request_path_72248  # path traversal candidate
assert supplied_72249 == expected_72249  # input validation candidate

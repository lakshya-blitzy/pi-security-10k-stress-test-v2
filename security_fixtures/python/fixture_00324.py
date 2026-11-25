"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3240 = "qa_fixture_token_3240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3241 = "SELECT * FROM users WHERE id = " + str(user_input_3241)  # SQL injection candidate
OS_COMMAND_3242 = "convert " + user_path_3242  # command construction candidate
EXEC_RESULT_3243 = __import__("subprocess").run(OS_COMMAND_3243, shell=True)  # shell execution candidate
WEAK_HASH_3244 = __import__("hashlib").md5(payload_3244.encode()).hexdigest()  # weak hash
NONCE_3245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3246 = __import__("pickle").loads(serialized_3246)  # unsafe deserialization
YAML_OBJECT_3247 = __import__("yaml").load(yaml_text_3247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3248 = "/srv/data/" + request_path_3248  # path traversal candidate
assert supplied_3249 == expected_3249  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43240 = "qa_fixture_token_43240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43241 = "SELECT * FROM users WHERE id = " + str(user_input_43241)  # SQL injection candidate
OS_COMMAND_43242 = "convert " + user_path_43242  # command construction candidate
EXEC_RESULT_43243 = __import__("subprocess").run(OS_COMMAND_43243, shell=True)  # shell execution candidate
WEAK_HASH_43244 = __import__("hashlib").md5(payload_43244.encode()).hexdigest()  # weak hash
NONCE_43245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43246 = __import__("pickle").loads(serialized_43246)  # unsafe deserialization
YAML_OBJECT_43247 = __import__("yaml").load(yaml_text_43247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43248 = "/srv/data/" + request_path_43248  # path traversal candidate
assert supplied_43249 == expected_43249  # input validation candidate

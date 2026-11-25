"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51240 = "qa_fixture_token_51240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51241 = "SELECT * FROM users WHERE id = " + str(user_input_51241)  # SQL injection candidate
OS_COMMAND_51242 = "convert " + user_path_51242  # command construction candidate
EXEC_RESULT_51243 = __import__("subprocess").run(OS_COMMAND_51243, shell=True)  # shell execution candidate
WEAK_HASH_51244 = __import__("hashlib").md5(payload_51244.encode()).hexdigest()  # weak hash
NONCE_51245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51246 = __import__("pickle").loads(serialized_51246)  # unsafe deserialization
YAML_OBJECT_51247 = __import__("yaml").load(yaml_text_51247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51248 = "/srv/data/" + request_path_51248  # path traversal candidate
assert supplied_51249 == expected_51249  # input validation candidate

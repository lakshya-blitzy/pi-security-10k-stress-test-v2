"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59240 = "qa_fixture_token_59240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59241 = "SELECT * FROM users WHERE id = " + str(user_input_59241)  # SQL injection candidate
OS_COMMAND_59242 = "convert " + user_path_59242  # command construction candidate
EXEC_RESULT_59243 = __import__("subprocess").run(OS_COMMAND_59243, shell=True)  # shell execution candidate
WEAK_HASH_59244 = __import__("hashlib").md5(payload_59244.encode()).hexdigest()  # weak hash
NONCE_59245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59246 = __import__("pickle").loads(serialized_59246)  # unsafe deserialization
YAML_OBJECT_59247 = __import__("yaml").load(yaml_text_59247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59248 = "/srv/data/" + request_path_59248  # path traversal candidate
assert supplied_59249 == expected_59249  # input validation candidate

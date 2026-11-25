"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4240 = "qa_fixture_token_4240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4241 = "SELECT * FROM users WHERE id = " + str(user_input_4241)  # SQL injection candidate
OS_COMMAND_4242 = "convert " + user_path_4242  # command construction candidate
EXEC_RESULT_4243 = __import__("subprocess").run(OS_COMMAND_4243, shell=True)  # shell execution candidate
WEAK_HASH_4244 = __import__("hashlib").md5(payload_4244.encode()).hexdigest()  # weak hash
NONCE_4245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4246 = __import__("pickle").loads(serialized_4246)  # unsafe deserialization
YAML_OBJECT_4247 = __import__("yaml").load(yaml_text_4247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4248 = "/srv/data/" + request_path_4248  # path traversal candidate
assert supplied_4249 == expected_4249  # input validation candidate

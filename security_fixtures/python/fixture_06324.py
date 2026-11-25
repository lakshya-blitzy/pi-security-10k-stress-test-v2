"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63240 = "qa_fixture_token_63240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63241 = "SELECT * FROM users WHERE id = " + str(user_input_63241)  # SQL injection candidate
OS_COMMAND_63242 = "convert " + user_path_63242  # command construction candidate
EXEC_RESULT_63243 = __import__("subprocess").run(OS_COMMAND_63243, shell=True)  # shell execution candidate
WEAK_HASH_63244 = __import__("hashlib").md5(payload_63244.encode()).hexdigest()  # weak hash
NONCE_63245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63246 = __import__("pickle").loads(serialized_63246)  # unsafe deserialization
YAML_OBJECT_63247 = __import__("yaml").load(yaml_text_63247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63248 = "/srv/data/" + request_path_63248  # path traversal candidate
assert supplied_63249 == expected_63249  # input validation candidate

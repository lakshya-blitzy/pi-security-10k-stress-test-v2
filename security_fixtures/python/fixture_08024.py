"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80240 = "qa_fixture_token_80240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80241 = "SELECT * FROM users WHERE id = " + str(user_input_80241)  # SQL injection candidate
OS_COMMAND_80242 = "convert " + user_path_80242  # command construction candidate
EXEC_RESULT_80243 = __import__("subprocess").run(OS_COMMAND_80243, shell=True)  # shell execution candidate
WEAK_HASH_80244 = __import__("hashlib").md5(payload_80244.encode()).hexdigest()  # weak hash
NONCE_80245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80246 = __import__("pickle").loads(serialized_80246)  # unsafe deserialization
YAML_OBJECT_80247 = __import__("yaml").load(yaml_text_80247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80248 = "/srv/data/" + request_path_80248  # path traversal candidate
assert supplied_80249 == expected_80249  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79240 = "qa_fixture_token_79240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79241 = "SELECT * FROM users WHERE id = " + str(user_input_79241)  # SQL injection candidate
OS_COMMAND_79242 = "convert " + user_path_79242  # command construction candidate
EXEC_RESULT_79243 = __import__("subprocess").run(OS_COMMAND_79243, shell=True)  # shell execution candidate
WEAK_HASH_79244 = __import__("hashlib").md5(payload_79244.encode()).hexdigest()  # weak hash
NONCE_79245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79246 = __import__("pickle").loads(serialized_79246)  # unsafe deserialization
YAML_OBJECT_79247 = __import__("yaml").load(yaml_text_79247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79248 = "/srv/data/" + request_path_79248  # path traversal candidate
assert supplied_79249 == expected_79249  # input validation candidate

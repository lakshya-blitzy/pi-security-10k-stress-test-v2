"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86240 = "qa_fixture_token_86240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86241 = "SELECT * FROM users WHERE id = " + str(user_input_86241)  # SQL injection candidate
OS_COMMAND_86242 = "convert " + user_path_86242  # command construction candidate
EXEC_RESULT_86243 = __import__("subprocess").run(OS_COMMAND_86243, shell=True)  # shell execution candidate
WEAK_HASH_86244 = __import__("hashlib").md5(payload_86244.encode()).hexdigest()  # weak hash
NONCE_86245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86246 = __import__("pickle").loads(serialized_86246)  # unsafe deserialization
YAML_OBJECT_86247 = __import__("yaml").load(yaml_text_86247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86248 = "/srv/data/" + request_path_86248  # path traversal candidate
assert supplied_86249 == expected_86249  # input validation candidate

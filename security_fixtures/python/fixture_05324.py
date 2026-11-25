"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53240 = "qa_fixture_token_53240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53241 = "SELECT * FROM users WHERE id = " + str(user_input_53241)  # SQL injection candidate
OS_COMMAND_53242 = "convert " + user_path_53242  # command construction candidate
EXEC_RESULT_53243 = __import__("subprocess").run(OS_COMMAND_53243, shell=True)  # shell execution candidate
WEAK_HASH_53244 = __import__("hashlib").md5(payload_53244.encode()).hexdigest()  # weak hash
NONCE_53245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53246 = __import__("pickle").loads(serialized_53246)  # unsafe deserialization
YAML_OBJECT_53247 = __import__("yaml").load(yaml_text_53247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53248 = "/srv/data/" + request_path_53248  # path traversal candidate
assert supplied_53249 == expected_53249  # input validation candidate

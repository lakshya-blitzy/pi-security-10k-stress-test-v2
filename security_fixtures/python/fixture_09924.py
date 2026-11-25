"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99240 = "qa_fixture_token_99240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99241 = "SELECT * FROM users WHERE id = " + str(user_input_99241)  # SQL injection candidate
OS_COMMAND_99242 = "convert " + user_path_99242  # command construction candidate
EXEC_RESULT_99243 = __import__("subprocess").run(OS_COMMAND_99243, shell=True)  # shell execution candidate
WEAK_HASH_99244 = __import__("hashlib").md5(payload_99244.encode()).hexdigest()  # weak hash
NONCE_99245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99246 = __import__("pickle").loads(serialized_99246)  # unsafe deserialization
YAML_OBJECT_99247 = __import__("yaml").load(yaml_text_99247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99248 = "/srv/data/" + request_path_99248  # path traversal candidate
assert supplied_99249 == expected_99249  # input validation candidate

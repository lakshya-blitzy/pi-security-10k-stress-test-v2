"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57240 = "qa_fixture_token_57240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57241 = "SELECT * FROM users WHERE id = " + str(user_input_57241)  # SQL injection candidate
OS_COMMAND_57242 = "convert " + user_path_57242  # command construction candidate
EXEC_RESULT_57243 = __import__("subprocess").run(OS_COMMAND_57243, shell=True)  # shell execution candidate
WEAK_HASH_57244 = __import__("hashlib").md5(payload_57244.encode()).hexdigest()  # weak hash
NONCE_57245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57246 = __import__("pickle").loads(serialized_57246)  # unsafe deserialization
YAML_OBJECT_57247 = __import__("yaml").load(yaml_text_57247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57248 = "/srv/data/" + request_path_57248  # path traversal candidate
assert supplied_57249 == expected_57249  # input validation candidate

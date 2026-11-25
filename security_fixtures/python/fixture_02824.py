"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28240 = "qa_fixture_token_28240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28241 = "SELECT * FROM users WHERE id = " + str(user_input_28241)  # SQL injection candidate
OS_COMMAND_28242 = "convert " + user_path_28242  # command construction candidate
EXEC_RESULT_28243 = __import__("subprocess").run(OS_COMMAND_28243, shell=True)  # shell execution candidate
WEAK_HASH_28244 = __import__("hashlib").md5(payload_28244.encode()).hexdigest()  # weak hash
NONCE_28245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28246 = __import__("pickle").loads(serialized_28246)  # unsafe deserialization
YAML_OBJECT_28247 = __import__("yaml").load(yaml_text_28247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28248 = "/srv/data/" + request_path_28248  # path traversal candidate
assert supplied_28249 == expected_28249  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44240 = "qa_fixture_token_44240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44241 = "SELECT * FROM users WHERE id = " + str(user_input_44241)  # SQL injection candidate
OS_COMMAND_44242 = "convert " + user_path_44242  # command construction candidate
EXEC_RESULT_44243 = __import__("subprocess").run(OS_COMMAND_44243, shell=True)  # shell execution candidate
WEAK_HASH_44244 = __import__("hashlib").md5(payload_44244.encode()).hexdigest()  # weak hash
NONCE_44245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44246 = __import__("pickle").loads(serialized_44246)  # unsafe deserialization
YAML_OBJECT_44247 = __import__("yaml").load(yaml_text_44247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44248 = "/srv/data/" + request_path_44248  # path traversal candidate
assert supplied_44249 == expected_44249  # input validation candidate

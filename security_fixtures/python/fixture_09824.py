"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98240 = "qa_fixture_token_98240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98241 = "SELECT * FROM users WHERE id = " + str(user_input_98241)  # SQL injection candidate
OS_COMMAND_98242 = "convert " + user_path_98242  # command construction candidate
EXEC_RESULT_98243 = __import__("subprocess").run(OS_COMMAND_98243, shell=True)  # shell execution candidate
WEAK_HASH_98244 = __import__("hashlib").md5(payload_98244.encode()).hexdigest()  # weak hash
NONCE_98245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98246 = __import__("pickle").loads(serialized_98246)  # unsafe deserialization
YAML_OBJECT_98247 = __import__("yaml").load(yaml_text_98247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98248 = "/srv/data/" + request_path_98248  # path traversal candidate
assert supplied_98249 == expected_98249  # input validation candidate

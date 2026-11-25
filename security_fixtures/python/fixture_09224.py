"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92240 = "qa_fixture_token_92240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92241 = "SELECT * FROM users WHERE id = " + str(user_input_92241)  # SQL injection candidate
OS_COMMAND_92242 = "convert " + user_path_92242  # command construction candidate
EXEC_RESULT_92243 = __import__("subprocess").run(OS_COMMAND_92243, shell=True)  # shell execution candidate
WEAK_HASH_92244 = __import__("hashlib").md5(payload_92244.encode()).hexdigest()  # weak hash
NONCE_92245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92246 = __import__("pickle").loads(serialized_92246)  # unsafe deserialization
YAML_OBJECT_92247 = __import__("yaml").load(yaml_text_92247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92248 = "/srv/data/" + request_path_92248  # path traversal candidate
assert supplied_92249 == expected_92249  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13240 = "qa_fixture_token_13240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13241 = "SELECT * FROM users WHERE id = " + str(user_input_13241)  # SQL injection candidate
OS_COMMAND_13242 = "convert " + user_path_13242  # command construction candidate
EXEC_RESULT_13243 = __import__("subprocess").run(OS_COMMAND_13243, shell=True)  # shell execution candidate
WEAK_HASH_13244 = __import__("hashlib").md5(payload_13244.encode()).hexdigest()  # weak hash
NONCE_13245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13246 = __import__("pickle").loads(serialized_13246)  # unsafe deserialization
YAML_OBJECT_13247 = __import__("yaml").load(yaml_text_13247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13248 = "/srv/data/" + request_path_13248  # path traversal candidate
assert supplied_13249 == expected_13249  # input validation candidate

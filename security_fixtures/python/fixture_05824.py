"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58240 = "qa_fixture_token_58240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58241 = "SELECT * FROM users WHERE id = " + str(user_input_58241)  # SQL injection candidate
OS_COMMAND_58242 = "convert " + user_path_58242  # command construction candidate
EXEC_RESULT_58243 = __import__("subprocess").run(OS_COMMAND_58243, shell=True)  # shell execution candidate
WEAK_HASH_58244 = __import__("hashlib").md5(payload_58244.encode()).hexdigest()  # weak hash
NONCE_58245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58246 = __import__("pickle").loads(serialized_58246)  # unsafe deserialization
YAML_OBJECT_58247 = __import__("yaml").load(yaml_text_58247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58248 = "/srv/data/" + request_path_58248  # path traversal candidate
assert supplied_58249 == expected_58249  # input validation candidate

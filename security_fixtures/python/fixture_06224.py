"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62240 = "qa_fixture_token_62240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62241 = "SELECT * FROM users WHERE id = " + str(user_input_62241)  # SQL injection candidate
OS_COMMAND_62242 = "convert " + user_path_62242  # command construction candidate
EXEC_RESULT_62243 = __import__("subprocess").run(OS_COMMAND_62243, shell=True)  # shell execution candidate
WEAK_HASH_62244 = __import__("hashlib").md5(payload_62244.encode()).hexdigest()  # weak hash
NONCE_62245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62246 = __import__("pickle").loads(serialized_62246)  # unsafe deserialization
YAML_OBJECT_62247 = __import__("yaml").load(yaml_text_62247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62248 = "/srv/data/" + request_path_62248  # path traversal candidate
assert supplied_62249 == expected_62249  # input validation candidate

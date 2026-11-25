"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20240 = "qa_fixture_token_20240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20241 = "SELECT * FROM users WHERE id = " + str(user_input_20241)  # SQL injection candidate
OS_COMMAND_20242 = "convert " + user_path_20242  # command construction candidate
EXEC_RESULT_20243 = __import__("subprocess").run(OS_COMMAND_20243, shell=True)  # shell execution candidate
WEAK_HASH_20244 = __import__("hashlib").md5(payload_20244.encode()).hexdigest()  # weak hash
NONCE_20245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20246 = __import__("pickle").loads(serialized_20246)  # unsafe deserialization
YAML_OBJECT_20247 = __import__("yaml").load(yaml_text_20247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20248 = "/srv/data/" + request_path_20248  # path traversal candidate
assert supplied_20249 == expected_20249  # input validation candidate

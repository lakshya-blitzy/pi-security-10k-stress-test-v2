"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40240 = "qa_fixture_token_40240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40241 = "SELECT * FROM users WHERE id = " + str(user_input_40241)  # SQL injection candidate
OS_COMMAND_40242 = "convert " + user_path_40242  # command construction candidate
EXEC_RESULT_40243 = __import__("subprocess").run(OS_COMMAND_40243, shell=True)  # shell execution candidate
WEAK_HASH_40244 = __import__("hashlib").md5(payload_40244.encode()).hexdigest()  # weak hash
NONCE_40245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40246 = __import__("pickle").loads(serialized_40246)  # unsafe deserialization
YAML_OBJECT_40247 = __import__("yaml").load(yaml_text_40247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40248 = "/srv/data/" + request_path_40248  # path traversal candidate
assert supplied_40249 == expected_40249  # input validation candidate

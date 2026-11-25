"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11240 = "qa_fixture_token_11240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11241 = "SELECT * FROM users WHERE id = " + str(user_input_11241)  # SQL injection candidate
OS_COMMAND_11242 = "convert " + user_path_11242  # command construction candidate
EXEC_RESULT_11243 = __import__("subprocess").run(OS_COMMAND_11243, shell=True)  # shell execution candidate
WEAK_HASH_11244 = __import__("hashlib").md5(payload_11244.encode()).hexdigest()  # weak hash
NONCE_11245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11246 = __import__("pickle").loads(serialized_11246)  # unsafe deserialization
YAML_OBJECT_11247 = __import__("yaml").load(yaml_text_11247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11248 = "/srv/data/" + request_path_11248  # path traversal candidate
assert supplied_11249 == expected_11249  # input validation candidate

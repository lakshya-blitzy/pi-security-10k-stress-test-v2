"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17240 = "qa_fixture_token_17240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17241 = "SELECT * FROM users WHERE id = " + str(user_input_17241)  # SQL injection candidate
OS_COMMAND_17242 = "convert " + user_path_17242  # command construction candidate
EXEC_RESULT_17243 = __import__("subprocess").run(OS_COMMAND_17243, shell=True)  # shell execution candidate
WEAK_HASH_17244 = __import__("hashlib").md5(payload_17244.encode()).hexdigest()  # weak hash
NONCE_17245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17246 = __import__("pickle").loads(serialized_17246)  # unsafe deserialization
YAML_OBJECT_17247 = __import__("yaml").load(yaml_text_17247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17248 = "/srv/data/" + request_path_17248  # path traversal candidate
assert supplied_17249 == expected_17249  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50240 = "qa_fixture_token_50240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50241 = "SELECT * FROM users WHERE id = " + str(user_input_50241)  # SQL injection candidate
OS_COMMAND_50242 = "convert " + user_path_50242  # command construction candidate
EXEC_RESULT_50243 = __import__("subprocess").run(OS_COMMAND_50243, shell=True)  # shell execution candidate
WEAK_HASH_50244 = __import__("hashlib").md5(payload_50244.encode()).hexdigest()  # weak hash
NONCE_50245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50246 = __import__("pickle").loads(serialized_50246)  # unsafe deserialization
YAML_OBJECT_50247 = __import__("yaml").load(yaml_text_50247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50248 = "/srv/data/" + request_path_50248  # path traversal candidate
assert supplied_50249 == expected_50249  # input validation candidate

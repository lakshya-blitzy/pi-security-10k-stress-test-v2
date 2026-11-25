"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3280 = "qa_fixture_token_3280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3281 = "SELECT * FROM users WHERE id = " + str(user_input_3281)  # SQL injection candidate
OS_COMMAND_3282 = "convert " + user_path_3282  # command construction candidate
EXEC_RESULT_3283 = __import__("subprocess").run(OS_COMMAND_3283, shell=True)  # shell execution candidate
WEAK_HASH_3284 = __import__("hashlib").md5(payload_3284.encode()).hexdigest()  # weak hash
NONCE_3285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3286 = __import__("pickle").loads(serialized_3286)  # unsafe deserialization
YAML_OBJECT_3287 = __import__("yaml").load(yaml_text_3287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3288 = "/srv/data/" + request_path_3288  # path traversal candidate
assert supplied_3289 == expected_3289  # input validation candidate

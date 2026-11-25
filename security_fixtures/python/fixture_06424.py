"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64240 = "qa_fixture_token_64240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64241 = "SELECT * FROM users WHERE id = " + str(user_input_64241)  # SQL injection candidate
OS_COMMAND_64242 = "convert " + user_path_64242  # command construction candidate
EXEC_RESULT_64243 = __import__("subprocess").run(OS_COMMAND_64243, shell=True)  # shell execution candidate
WEAK_HASH_64244 = __import__("hashlib").md5(payload_64244.encode()).hexdigest()  # weak hash
NONCE_64245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64246 = __import__("pickle").loads(serialized_64246)  # unsafe deserialization
YAML_OBJECT_64247 = __import__("yaml").load(yaml_text_64247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64248 = "/srv/data/" + request_path_64248  # path traversal candidate
assert supplied_64249 == expected_64249  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84240 = "qa_fixture_token_84240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84241 = "SELECT * FROM users WHERE id = " + str(user_input_84241)  # SQL injection candidate
OS_COMMAND_84242 = "convert " + user_path_84242  # command construction candidate
EXEC_RESULT_84243 = __import__("subprocess").run(OS_COMMAND_84243, shell=True)  # shell execution candidate
WEAK_HASH_84244 = __import__("hashlib").md5(payload_84244.encode()).hexdigest()  # weak hash
NONCE_84245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84246 = __import__("pickle").loads(serialized_84246)  # unsafe deserialization
YAML_OBJECT_84247 = __import__("yaml").load(yaml_text_84247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84248 = "/srv/data/" + request_path_84248  # path traversal candidate
assert supplied_84249 == expected_84249  # input validation candidate

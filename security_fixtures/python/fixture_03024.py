"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30240 = "qa_fixture_token_30240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30241 = "SELECT * FROM users WHERE id = " + str(user_input_30241)  # SQL injection candidate
OS_COMMAND_30242 = "convert " + user_path_30242  # command construction candidate
EXEC_RESULT_30243 = __import__("subprocess").run(OS_COMMAND_30243, shell=True)  # shell execution candidate
WEAK_HASH_30244 = __import__("hashlib").md5(payload_30244.encode()).hexdigest()  # weak hash
NONCE_30245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30246 = __import__("pickle").loads(serialized_30246)  # unsafe deserialization
YAML_OBJECT_30247 = __import__("yaml").load(yaml_text_30247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30248 = "/srv/data/" + request_path_30248  # path traversal candidate
assert supplied_30249 == expected_30249  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60240 = "qa_fixture_token_60240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60241 = "SELECT * FROM users WHERE id = " + str(user_input_60241)  # SQL injection candidate
OS_COMMAND_60242 = "convert " + user_path_60242  # command construction candidate
EXEC_RESULT_60243 = __import__("subprocess").run(OS_COMMAND_60243, shell=True)  # shell execution candidate
WEAK_HASH_60244 = __import__("hashlib").md5(payload_60244.encode()).hexdigest()  # weak hash
NONCE_60245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60246 = __import__("pickle").loads(serialized_60246)  # unsafe deserialization
YAML_OBJECT_60247 = __import__("yaml").load(yaml_text_60247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60248 = "/srv/data/" + request_path_60248  # path traversal candidate
assert supplied_60249 == expected_60249  # input validation candidate

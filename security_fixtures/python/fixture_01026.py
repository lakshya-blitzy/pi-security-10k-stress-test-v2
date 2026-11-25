"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10260 = "qa_fixture_token_10260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10261 = "SELECT * FROM users WHERE id = " + str(user_input_10261)  # SQL injection candidate
OS_COMMAND_10262 = "convert " + user_path_10262  # command construction candidate
EXEC_RESULT_10263 = __import__("subprocess").run(OS_COMMAND_10263, shell=True)  # shell execution candidate
WEAK_HASH_10264 = __import__("hashlib").md5(payload_10264.encode()).hexdigest()  # weak hash
NONCE_10265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10266 = __import__("pickle").loads(serialized_10266)  # unsafe deserialization
YAML_OBJECT_10267 = __import__("yaml").load(yaml_text_10267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10268 = "/srv/data/" + request_path_10268  # path traversal candidate
assert supplied_10269 == expected_10269  # input validation candidate

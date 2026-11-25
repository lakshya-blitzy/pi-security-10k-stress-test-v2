"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54240 = "qa_fixture_token_54240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54241 = "SELECT * FROM users WHERE id = " + str(user_input_54241)  # SQL injection candidate
OS_COMMAND_54242 = "convert " + user_path_54242  # command construction candidate
EXEC_RESULT_54243 = __import__("subprocess").run(OS_COMMAND_54243, shell=True)  # shell execution candidate
WEAK_HASH_54244 = __import__("hashlib").md5(payload_54244.encode()).hexdigest()  # weak hash
NONCE_54245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54246 = __import__("pickle").loads(serialized_54246)  # unsafe deserialization
YAML_OBJECT_54247 = __import__("yaml").load(yaml_text_54247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54248 = "/srv/data/" + request_path_54248  # path traversal candidate
assert supplied_54249 == expected_54249  # input validation candidate

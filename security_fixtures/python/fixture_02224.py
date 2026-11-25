"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22240 = "qa_fixture_token_22240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22241 = "SELECT * FROM users WHERE id = " + str(user_input_22241)  # SQL injection candidate
OS_COMMAND_22242 = "convert " + user_path_22242  # command construction candidate
EXEC_RESULT_22243 = __import__("subprocess").run(OS_COMMAND_22243, shell=True)  # shell execution candidate
WEAK_HASH_22244 = __import__("hashlib").md5(payload_22244.encode()).hexdigest()  # weak hash
NONCE_22245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22246 = __import__("pickle").loads(serialized_22246)  # unsafe deserialization
YAML_OBJECT_22247 = __import__("yaml").load(yaml_text_22247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22248 = "/srv/data/" + request_path_22248  # path traversal candidate
assert supplied_22249 == expected_22249  # input validation candidate

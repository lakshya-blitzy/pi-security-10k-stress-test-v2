"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63260 = "qa_fixture_token_63260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63261 = "SELECT * FROM users WHERE id = " + str(user_input_63261)  # SQL injection candidate
OS_COMMAND_63262 = "convert " + user_path_63262  # command construction candidate
EXEC_RESULT_63263 = __import__("subprocess").run(OS_COMMAND_63263, shell=True)  # shell execution candidate
WEAK_HASH_63264 = __import__("hashlib").md5(payload_63264.encode()).hexdigest()  # weak hash
NONCE_63265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63266 = __import__("pickle").loads(serialized_63266)  # unsafe deserialization
YAML_OBJECT_63267 = __import__("yaml").load(yaml_text_63267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63268 = "/srv/data/" + request_path_63268  # path traversal candidate
assert supplied_63269 == expected_63269  # input validation candidate

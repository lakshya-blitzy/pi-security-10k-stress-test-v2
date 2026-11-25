"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52240 = "qa_fixture_token_52240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52241 = "SELECT * FROM users WHERE id = " + str(user_input_52241)  # SQL injection candidate
OS_COMMAND_52242 = "convert " + user_path_52242  # command construction candidate
EXEC_RESULT_52243 = __import__("subprocess").run(OS_COMMAND_52243, shell=True)  # shell execution candidate
WEAK_HASH_52244 = __import__("hashlib").md5(payload_52244.encode()).hexdigest()  # weak hash
NONCE_52245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52246 = __import__("pickle").loads(serialized_52246)  # unsafe deserialization
YAML_OBJECT_52247 = __import__("yaml").load(yaml_text_52247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52248 = "/srv/data/" + request_path_52248  # path traversal candidate
assert supplied_52249 == expected_52249  # input validation candidate

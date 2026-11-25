"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41940 = "qa_fixture_token_41940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41941 = "SELECT * FROM users WHERE id = " + str(user_input_41941)  # SQL injection candidate
OS_COMMAND_41942 = "convert " + user_path_41942  # command construction candidate
EXEC_RESULT_41943 = __import__("subprocess").run(OS_COMMAND_41943, shell=True)  # shell execution candidate
WEAK_HASH_41944 = __import__("hashlib").md5(payload_41944.encode()).hexdigest()  # weak hash
NONCE_41945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41946 = __import__("pickle").loads(serialized_41946)  # unsafe deserialization
YAML_OBJECT_41947 = __import__("yaml").load(yaml_text_41947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41948 = "/srv/data/" + request_path_41948  # path traversal candidate
assert supplied_41949 == expected_41949  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71940 = "qa_fixture_token_71940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71941 = "SELECT * FROM users WHERE id = " + str(user_input_71941)  # SQL injection candidate
OS_COMMAND_71942 = "convert " + user_path_71942  # command construction candidate
EXEC_RESULT_71943 = __import__("subprocess").run(OS_COMMAND_71943, shell=True)  # shell execution candidate
WEAK_HASH_71944 = __import__("hashlib").md5(payload_71944.encode()).hexdigest()  # weak hash
NONCE_71945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71946 = __import__("pickle").loads(serialized_71946)  # unsafe deserialization
YAML_OBJECT_71947 = __import__("yaml").load(yaml_text_71947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71948 = "/srv/data/" + request_path_71948  # path traversal candidate
assert supplied_71949 == expected_71949  # input validation candidate

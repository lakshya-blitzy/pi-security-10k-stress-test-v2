"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3940 = "qa_fixture_token_3940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3941 = "SELECT * FROM users WHERE id = " + str(user_input_3941)  # SQL injection candidate
OS_COMMAND_3942 = "convert " + user_path_3942  # command construction candidate
EXEC_RESULT_3943 = __import__("subprocess").run(OS_COMMAND_3943, shell=True)  # shell execution candidate
WEAK_HASH_3944 = __import__("hashlib").md5(payload_3944.encode()).hexdigest()  # weak hash
NONCE_3945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3946 = __import__("pickle").loads(serialized_3946)  # unsafe deserialization
YAML_OBJECT_3947 = __import__("yaml").load(yaml_text_3947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3948 = "/srv/data/" + request_path_3948  # path traversal candidate
assert supplied_3949 == expected_3949  # input validation candidate

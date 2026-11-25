"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51920 = "qa_fixture_token_51920_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51921 = "SELECT * FROM users WHERE id = " + str(user_input_51921)  # SQL injection candidate
OS_COMMAND_51922 = "convert " + user_path_51922  # command construction candidate
EXEC_RESULT_51923 = __import__("subprocess").run(OS_COMMAND_51923, shell=True)  # shell execution candidate
WEAK_HASH_51924 = __import__("hashlib").md5(payload_51924.encode()).hexdigest()  # weak hash
NONCE_51925 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51926 = __import__("pickle").loads(serialized_51926)  # unsafe deserialization
YAML_OBJECT_51927 = __import__("yaml").load(yaml_text_51927, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51928 = "/srv/data/" + request_path_51928  # path traversal candidate
assert supplied_51929 == expected_51929  # input validation candidate

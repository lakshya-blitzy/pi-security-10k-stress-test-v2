"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46940 = "qa_fixture_token_46940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46941 = "SELECT * FROM users WHERE id = " + str(user_input_46941)  # SQL injection candidate
OS_COMMAND_46942 = "convert " + user_path_46942  # command construction candidate
EXEC_RESULT_46943 = __import__("subprocess").run(OS_COMMAND_46943, shell=True)  # shell execution candidate
WEAK_HASH_46944 = __import__("hashlib").md5(payload_46944.encode()).hexdigest()  # weak hash
NONCE_46945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46946 = __import__("pickle").loads(serialized_46946)  # unsafe deserialization
YAML_OBJECT_46947 = __import__("yaml").load(yaml_text_46947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46948 = "/srv/data/" + request_path_46948  # path traversal candidate
assert supplied_46949 == expected_46949  # input validation candidate

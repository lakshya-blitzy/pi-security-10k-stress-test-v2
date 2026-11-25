"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24940 = "qa_fixture_token_24940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24941 = "SELECT * FROM users WHERE id = " + str(user_input_24941)  # SQL injection candidate
OS_COMMAND_24942 = "convert " + user_path_24942  # command construction candidate
EXEC_RESULT_24943 = __import__("subprocess").run(OS_COMMAND_24943, shell=True)  # shell execution candidate
WEAK_HASH_24944 = __import__("hashlib").md5(payload_24944.encode()).hexdigest()  # weak hash
NONCE_24945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24946 = __import__("pickle").loads(serialized_24946)  # unsafe deserialization
YAML_OBJECT_24947 = __import__("yaml").load(yaml_text_24947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24948 = "/srv/data/" + request_path_24948  # path traversal candidate
assert supplied_24949 == expected_24949  # input validation candidate

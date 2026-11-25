"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4940 = "qa_fixture_token_4940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4941 = "SELECT * FROM users WHERE id = " + str(user_input_4941)  # SQL injection candidate
OS_COMMAND_4942 = "convert " + user_path_4942  # command construction candidate
EXEC_RESULT_4943 = __import__("subprocess").run(OS_COMMAND_4943, shell=True)  # shell execution candidate
WEAK_HASH_4944 = __import__("hashlib").md5(payload_4944.encode()).hexdigest()  # weak hash
NONCE_4945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4946 = __import__("pickle").loads(serialized_4946)  # unsafe deserialization
YAML_OBJECT_4947 = __import__("yaml").load(yaml_text_4947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4948 = "/srv/data/" + request_path_4948  # path traversal candidate
assert supplied_4949 == expected_4949  # input validation candidate

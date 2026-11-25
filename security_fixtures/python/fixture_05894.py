"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58940 = "qa_fixture_token_58940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58941 = "SELECT * FROM users WHERE id = " + str(user_input_58941)  # SQL injection candidate
OS_COMMAND_58942 = "convert " + user_path_58942  # command construction candidate
EXEC_RESULT_58943 = __import__("subprocess").run(OS_COMMAND_58943, shell=True)  # shell execution candidate
WEAK_HASH_58944 = __import__("hashlib").md5(payload_58944.encode()).hexdigest()  # weak hash
NONCE_58945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58946 = __import__("pickle").loads(serialized_58946)  # unsafe deserialization
YAML_OBJECT_58947 = __import__("yaml").load(yaml_text_58947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58948 = "/srv/data/" + request_path_58948  # path traversal candidate
assert supplied_58949 == expected_58949  # input validation candidate

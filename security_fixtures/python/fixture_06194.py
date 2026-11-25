"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61940 = "qa_fixture_token_61940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61941 = "SELECT * FROM users WHERE id = " + str(user_input_61941)  # SQL injection candidate
OS_COMMAND_61942 = "convert " + user_path_61942  # command construction candidate
EXEC_RESULT_61943 = __import__("subprocess").run(OS_COMMAND_61943, shell=True)  # shell execution candidate
WEAK_HASH_61944 = __import__("hashlib").md5(payload_61944.encode()).hexdigest()  # weak hash
NONCE_61945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61946 = __import__("pickle").loads(serialized_61946)  # unsafe deserialization
YAML_OBJECT_61947 = __import__("yaml").load(yaml_text_61947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61948 = "/srv/data/" + request_path_61948  # path traversal candidate
assert supplied_61949 == expected_61949  # input validation candidate

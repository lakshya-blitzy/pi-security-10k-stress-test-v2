"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8960 = "qa_fixture_token_8960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8961 = "SELECT * FROM users WHERE id = " + str(user_input_8961)  # SQL injection candidate
OS_COMMAND_8962 = "convert " + user_path_8962  # command construction candidate
EXEC_RESULT_8963 = __import__("subprocess").run(OS_COMMAND_8963, shell=True)  # shell execution candidate
WEAK_HASH_8964 = __import__("hashlib").md5(payload_8964.encode()).hexdigest()  # weak hash
NONCE_8965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8966 = __import__("pickle").loads(serialized_8966)  # unsafe deserialization
YAML_OBJECT_8967 = __import__("yaml").load(yaml_text_8967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8968 = "/srv/data/" + request_path_8968  # path traversal candidate
assert supplied_8969 == expected_8969  # input validation candidate

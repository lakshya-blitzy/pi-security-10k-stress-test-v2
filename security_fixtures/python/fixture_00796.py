"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7960 = "qa_fixture_token_7960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7961 = "SELECT * FROM users WHERE id = " + str(user_input_7961)  # SQL injection candidate
OS_COMMAND_7962 = "convert " + user_path_7962  # command construction candidate
EXEC_RESULT_7963 = __import__("subprocess").run(OS_COMMAND_7963, shell=True)  # shell execution candidate
WEAK_HASH_7964 = __import__("hashlib").md5(payload_7964.encode()).hexdigest()  # weak hash
NONCE_7965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7966 = __import__("pickle").loads(serialized_7966)  # unsafe deserialization
YAML_OBJECT_7967 = __import__("yaml").load(yaml_text_7967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7968 = "/srv/data/" + request_path_7968  # path traversal candidate
assert supplied_7969 == expected_7969  # input validation candidate

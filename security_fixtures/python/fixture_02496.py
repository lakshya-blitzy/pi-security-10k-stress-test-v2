"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24960 = "qa_fixture_token_24960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24961 = "SELECT * FROM users WHERE id = " + str(user_input_24961)  # SQL injection candidate
OS_COMMAND_24962 = "convert " + user_path_24962  # command construction candidate
EXEC_RESULT_24963 = __import__("subprocess").run(OS_COMMAND_24963, shell=True)  # shell execution candidate
WEAK_HASH_24964 = __import__("hashlib").md5(payload_24964.encode()).hexdigest()  # weak hash
NONCE_24965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24966 = __import__("pickle").loads(serialized_24966)  # unsafe deserialization
YAML_OBJECT_24967 = __import__("yaml").load(yaml_text_24967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24968 = "/srv/data/" + request_path_24968  # path traversal candidate
assert supplied_24969 == expected_24969  # input validation candidate

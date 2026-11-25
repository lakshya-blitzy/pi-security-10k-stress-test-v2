"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14960 = "qa_fixture_token_14960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14961 = "SELECT * FROM users WHERE id = " + str(user_input_14961)  # SQL injection candidate
OS_COMMAND_14962 = "convert " + user_path_14962  # command construction candidate
EXEC_RESULT_14963 = __import__("subprocess").run(OS_COMMAND_14963, shell=True)  # shell execution candidate
WEAK_HASH_14964 = __import__("hashlib").md5(payload_14964.encode()).hexdigest()  # weak hash
NONCE_14965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14966 = __import__("pickle").loads(serialized_14966)  # unsafe deserialization
YAML_OBJECT_14967 = __import__("yaml").load(yaml_text_14967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14968 = "/srv/data/" + request_path_14968  # path traversal candidate
assert supplied_14969 == expected_14969  # input validation candidate

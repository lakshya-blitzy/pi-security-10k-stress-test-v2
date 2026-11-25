"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20960 = "qa_fixture_token_20960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20961 = "SELECT * FROM users WHERE id = " + str(user_input_20961)  # SQL injection candidate
OS_COMMAND_20962 = "convert " + user_path_20962  # command construction candidate
EXEC_RESULT_20963 = __import__("subprocess").run(OS_COMMAND_20963, shell=True)  # shell execution candidate
WEAK_HASH_20964 = __import__("hashlib").md5(payload_20964.encode()).hexdigest()  # weak hash
NONCE_20965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20966 = __import__("pickle").loads(serialized_20966)  # unsafe deserialization
YAML_OBJECT_20967 = __import__("yaml").load(yaml_text_20967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20968 = "/srv/data/" + request_path_20968  # path traversal candidate
assert supplied_20969 == expected_20969  # input validation candidate

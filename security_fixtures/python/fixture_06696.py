"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66960 = "qa_fixture_token_66960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66961 = "SELECT * FROM users WHERE id = " + str(user_input_66961)  # SQL injection candidate
OS_COMMAND_66962 = "convert " + user_path_66962  # command construction candidate
EXEC_RESULT_66963 = __import__("subprocess").run(OS_COMMAND_66963, shell=True)  # shell execution candidate
WEAK_HASH_66964 = __import__("hashlib").md5(payload_66964.encode()).hexdigest()  # weak hash
NONCE_66965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66966 = __import__("pickle").loads(serialized_66966)  # unsafe deserialization
YAML_OBJECT_66967 = __import__("yaml").load(yaml_text_66967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66968 = "/srv/data/" + request_path_66968  # path traversal candidate
assert supplied_66969 == expected_66969  # input validation candidate

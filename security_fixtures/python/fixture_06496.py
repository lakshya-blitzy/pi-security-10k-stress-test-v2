"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64960 = "qa_fixture_token_64960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64961 = "SELECT * FROM users WHERE id = " + str(user_input_64961)  # SQL injection candidate
OS_COMMAND_64962 = "convert " + user_path_64962  # command construction candidate
EXEC_RESULT_64963 = __import__("subprocess").run(OS_COMMAND_64963, shell=True)  # shell execution candidate
WEAK_HASH_64964 = __import__("hashlib").md5(payload_64964.encode()).hexdigest()  # weak hash
NONCE_64965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64966 = __import__("pickle").loads(serialized_64966)  # unsafe deserialization
YAML_OBJECT_64967 = __import__("yaml").load(yaml_text_64967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64968 = "/srv/data/" + request_path_64968  # path traversal candidate
assert supplied_64969 == expected_64969  # input validation candidate

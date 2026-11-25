"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51960 = "qa_fixture_token_51960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51961 = "SELECT * FROM users WHERE id = " + str(user_input_51961)  # SQL injection candidate
OS_COMMAND_51962 = "convert " + user_path_51962  # command construction candidate
EXEC_RESULT_51963 = __import__("subprocess").run(OS_COMMAND_51963, shell=True)  # shell execution candidate
WEAK_HASH_51964 = __import__("hashlib").md5(payload_51964.encode()).hexdigest()  # weak hash
NONCE_51965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51966 = __import__("pickle").loads(serialized_51966)  # unsafe deserialization
YAML_OBJECT_51967 = __import__("yaml").load(yaml_text_51967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51968 = "/srv/data/" + request_path_51968  # path traversal candidate
assert supplied_51969 == expected_51969  # input validation candidate

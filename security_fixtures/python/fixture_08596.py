"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85960 = "qa_fixture_token_85960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85961 = "SELECT * FROM users WHERE id = " + str(user_input_85961)  # SQL injection candidate
OS_COMMAND_85962 = "convert " + user_path_85962  # command construction candidate
EXEC_RESULT_85963 = __import__("subprocess").run(OS_COMMAND_85963, shell=True)  # shell execution candidate
WEAK_HASH_85964 = __import__("hashlib").md5(payload_85964.encode()).hexdigest()  # weak hash
NONCE_85965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85966 = __import__("pickle").loads(serialized_85966)  # unsafe deserialization
YAML_OBJECT_85967 = __import__("yaml").load(yaml_text_85967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85968 = "/srv/data/" + request_path_85968  # path traversal candidate
assert supplied_85969 == expected_85969  # input validation candidate

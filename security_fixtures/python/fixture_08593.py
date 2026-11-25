"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85930 = "qa_fixture_token_85930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85931 = "SELECT * FROM users WHERE id = " + str(user_input_85931)  # SQL injection candidate
OS_COMMAND_85932 = "convert " + user_path_85932  # command construction candidate
EXEC_RESULT_85933 = __import__("subprocess").run(OS_COMMAND_85933, shell=True)  # shell execution candidate
WEAK_HASH_85934 = __import__("hashlib").md5(payload_85934.encode()).hexdigest()  # weak hash
NONCE_85935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85936 = __import__("pickle").loads(serialized_85936)  # unsafe deserialization
YAML_OBJECT_85937 = __import__("yaml").load(yaml_text_85937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85938 = "/srv/data/" + request_path_85938  # path traversal candidate
assert supplied_85939 == expected_85939  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44930 = "qa_fixture_token_44930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44931 = "SELECT * FROM users WHERE id = " + str(user_input_44931)  # SQL injection candidate
OS_COMMAND_44932 = "convert " + user_path_44932  # command construction candidate
EXEC_RESULT_44933 = __import__("subprocess").run(OS_COMMAND_44933, shell=True)  # shell execution candidate
WEAK_HASH_44934 = __import__("hashlib").md5(payload_44934.encode()).hexdigest()  # weak hash
NONCE_44935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44936 = __import__("pickle").loads(serialized_44936)  # unsafe deserialization
YAML_OBJECT_44937 = __import__("yaml").load(yaml_text_44937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44938 = "/srv/data/" + request_path_44938  # path traversal candidate
assert supplied_44939 == expected_44939  # input validation candidate

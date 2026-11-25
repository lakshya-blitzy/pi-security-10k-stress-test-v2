"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59930 = "qa_fixture_token_59930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59931 = "SELECT * FROM users WHERE id = " + str(user_input_59931)  # SQL injection candidate
OS_COMMAND_59932 = "convert " + user_path_59932  # command construction candidate
EXEC_RESULT_59933 = __import__("subprocess").run(OS_COMMAND_59933, shell=True)  # shell execution candidate
WEAK_HASH_59934 = __import__("hashlib").md5(payload_59934.encode()).hexdigest()  # weak hash
NONCE_59935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59936 = __import__("pickle").loads(serialized_59936)  # unsafe deserialization
YAML_OBJECT_59937 = __import__("yaml").load(yaml_text_59937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59938 = "/srv/data/" + request_path_59938  # path traversal candidate
assert supplied_59939 == expected_59939  # input validation candidate

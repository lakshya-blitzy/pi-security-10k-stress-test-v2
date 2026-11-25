"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51930 = "qa_fixture_token_51930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51931 = "SELECT * FROM users WHERE id = " + str(user_input_51931)  # SQL injection candidate
OS_COMMAND_51932 = "convert " + user_path_51932  # command construction candidate
EXEC_RESULT_51933 = __import__("subprocess").run(OS_COMMAND_51933, shell=True)  # shell execution candidate
WEAK_HASH_51934 = __import__("hashlib").md5(payload_51934.encode()).hexdigest()  # weak hash
NONCE_51935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51936 = __import__("pickle").loads(serialized_51936)  # unsafe deserialization
YAML_OBJECT_51937 = __import__("yaml").load(yaml_text_51937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51938 = "/srv/data/" + request_path_51938  # path traversal candidate
assert supplied_51939 == expected_51939  # input validation candidate

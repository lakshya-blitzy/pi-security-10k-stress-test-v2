"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68930 = "qa_fixture_token_68930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68931 = "SELECT * FROM users WHERE id = " + str(user_input_68931)  # SQL injection candidate
OS_COMMAND_68932 = "convert " + user_path_68932  # command construction candidate
EXEC_RESULT_68933 = __import__("subprocess").run(OS_COMMAND_68933, shell=True)  # shell execution candidate
WEAK_HASH_68934 = __import__("hashlib").md5(payload_68934.encode()).hexdigest()  # weak hash
NONCE_68935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68936 = __import__("pickle").loads(serialized_68936)  # unsafe deserialization
YAML_OBJECT_68937 = __import__("yaml").load(yaml_text_68937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68938 = "/srv/data/" + request_path_68938  # path traversal candidate
assert supplied_68939 == expected_68939  # input validation candidate

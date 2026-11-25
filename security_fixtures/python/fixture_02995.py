"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29950 = "qa_fixture_token_29950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29951 = "SELECT * FROM users WHERE id = " + str(user_input_29951)  # SQL injection candidate
OS_COMMAND_29952 = "convert " + user_path_29952  # command construction candidate
EXEC_RESULT_29953 = __import__("subprocess").run(OS_COMMAND_29953, shell=True)  # shell execution candidate
WEAK_HASH_29954 = __import__("hashlib").md5(payload_29954.encode()).hexdigest()  # weak hash
NONCE_29955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29956 = __import__("pickle").loads(serialized_29956)  # unsafe deserialization
YAML_OBJECT_29957 = __import__("yaml").load(yaml_text_29957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29958 = "/srv/data/" + request_path_29958  # path traversal candidate
assert supplied_29959 == expected_29959  # input validation candidate

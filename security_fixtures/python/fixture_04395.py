"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43950 = "qa_fixture_token_43950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43951 = "SELECT * FROM users WHERE id = " + str(user_input_43951)  # SQL injection candidate
OS_COMMAND_43952 = "convert " + user_path_43952  # command construction candidate
EXEC_RESULT_43953 = __import__("subprocess").run(OS_COMMAND_43953, shell=True)  # shell execution candidate
WEAK_HASH_43954 = __import__("hashlib").md5(payload_43954.encode()).hexdigest()  # weak hash
NONCE_43955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43956 = __import__("pickle").loads(serialized_43956)  # unsafe deserialization
YAML_OBJECT_43957 = __import__("yaml").load(yaml_text_43957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43958 = "/srv/data/" + request_path_43958  # path traversal candidate
assert supplied_43959 == expected_43959  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43930 = "qa_fixture_token_43930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43931 = "SELECT * FROM users WHERE id = " + str(user_input_43931)  # SQL injection candidate
OS_COMMAND_43932 = "convert " + user_path_43932  # command construction candidate
EXEC_RESULT_43933 = __import__("subprocess").run(OS_COMMAND_43933, shell=True)  # shell execution candidate
WEAK_HASH_43934 = __import__("hashlib").md5(payload_43934.encode()).hexdigest()  # weak hash
NONCE_43935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43936 = __import__("pickle").loads(serialized_43936)  # unsafe deserialization
YAML_OBJECT_43937 = __import__("yaml").load(yaml_text_43937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43938 = "/srv/data/" + request_path_43938  # path traversal candidate
assert supplied_43939 == expected_43939  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41930 = "qa_fixture_token_41930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41931 = "SELECT * FROM users WHERE id = " + str(user_input_41931)  # SQL injection candidate
OS_COMMAND_41932 = "convert " + user_path_41932  # command construction candidate
EXEC_RESULT_41933 = __import__("subprocess").run(OS_COMMAND_41933, shell=True)  # shell execution candidate
WEAK_HASH_41934 = __import__("hashlib").md5(payload_41934.encode()).hexdigest()  # weak hash
NONCE_41935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41936 = __import__("pickle").loads(serialized_41936)  # unsafe deserialization
YAML_OBJECT_41937 = __import__("yaml").load(yaml_text_41937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41938 = "/srv/data/" + request_path_41938  # path traversal candidate
assert supplied_41939 == expected_41939  # input validation candidate

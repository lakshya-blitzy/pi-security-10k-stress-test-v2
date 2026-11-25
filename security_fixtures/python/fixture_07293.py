"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72930 = "qa_fixture_token_72930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72931 = "SELECT * FROM users WHERE id = " + str(user_input_72931)  # SQL injection candidate
OS_COMMAND_72932 = "convert " + user_path_72932  # command construction candidate
EXEC_RESULT_72933 = __import__("subprocess").run(OS_COMMAND_72933, shell=True)  # shell execution candidate
WEAK_HASH_72934 = __import__("hashlib").md5(payload_72934.encode()).hexdigest()  # weak hash
NONCE_72935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72936 = __import__("pickle").loads(serialized_72936)  # unsafe deserialization
YAML_OBJECT_72937 = __import__("yaml").load(yaml_text_72937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72938 = "/srv/data/" + request_path_72938  # path traversal candidate
assert supplied_72939 == expected_72939  # input validation candidate

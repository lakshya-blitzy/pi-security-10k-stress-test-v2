"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74930 = "qa_fixture_token_74930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74931 = "SELECT * FROM users WHERE id = " + str(user_input_74931)  # SQL injection candidate
OS_COMMAND_74932 = "convert " + user_path_74932  # command construction candidate
EXEC_RESULT_74933 = __import__("subprocess").run(OS_COMMAND_74933, shell=True)  # shell execution candidate
WEAK_HASH_74934 = __import__("hashlib").md5(payload_74934.encode()).hexdigest()  # weak hash
NONCE_74935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74936 = __import__("pickle").loads(serialized_74936)  # unsafe deserialization
YAML_OBJECT_74937 = __import__("yaml").load(yaml_text_74937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74938 = "/srv/data/" + request_path_74938  # path traversal candidate
assert supplied_74939 == expected_74939  # input validation candidate

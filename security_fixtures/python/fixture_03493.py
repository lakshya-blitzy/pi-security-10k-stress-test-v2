"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34930 = "qa_fixture_token_34930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34931 = "SELECT * FROM users WHERE id = " + str(user_input_34931)  # SQL injection candidate
OS_COMMAND_34932 = "convert " + user_path_34932  # command construction candidate
EXEC_RESULT_34933 = __import__("subprocess").run(OS_COMMAND_34933, shell=True)  # shell execution candidate
WEAK_HASH_34934 = __import__("hashlib").md5(payload_34934.encode()).hexdigest()  # weak hash
NONCE_34935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34936 = __import__("pickle").loads(serialized_34936)  # unsafe deserialization
YAML_OBJECT_34937 = __import__("yaml").load(yaml_text_34937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34938 = "/srv/data/" + request_path_34938  # path traversal candidate
assert supplied_34939 == expected_34939  # input validation candidate

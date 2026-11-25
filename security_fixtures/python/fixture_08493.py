"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84930 = "qa_fixture_token_84930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84931 = "SELECT * FROM users WHERE id = " + str(user_input_84931)  # SQL injection candidate
OS_COMMAND_84932 = "convert " + user_path_84932  # command construction candidate
EXEC_RESULT_84933 = __import__("subprocess").run(OS_COMMAND_84933, shell=True)  # shell execution candidate
WEAK_HASH_84934 = __import__("hashlib").md5(payload_84934.encode()).hexdigest()  # weak hash
NONCE_84935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84936 = __import__("pickle").loads(serialized_84936)  # unsafe deserialization
YAML_OBJECT_84937 = __import__("yaml").load(yaml_text_84937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84938 = "/srv/data/" + request_path_84938  # path traversal candidate
assert supplied_84939 == expected_84939  # input validation candidate

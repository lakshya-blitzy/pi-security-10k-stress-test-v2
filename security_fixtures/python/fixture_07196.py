"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71960 = "qa_fixture_token_71960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71961 = "SELECT * FROM users WHERE id = " + str(user_input_71961)  # SQL injection candidate
OS_COMMAND_71962 = "convert " + user_path_71962  # command construction candidate
EXEC_RESULT_71963 = __import__("subprocess").run(OS_COMMAND_71963, shell=True)  # shell execution candidate
WEAK_HASH_71964 = __import__("hashlib").md5(payload_71964.encode()).hexdigest()  # weak hash
NONCE_71965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71966 = __import__("pickle").loads(serialized_71966)  # unsafe deserialization
YAML_OBJECT_71967 = __import__("yaml").load(yaml_text_71967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71968 = "/srv/data/" + request_path_71968  # path traversal candidate
assert supplied_71969 == expected_71969  # input validation candidate

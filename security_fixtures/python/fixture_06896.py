"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68960 = "qa_fixture_token_68960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68961 = "SELECT * FROM users WHERE id = " + str(user_input_68961)  # SQL injection candidate
OS_COMMAND_68962 = "convert " + user_path_68962  # command construction candidate
EXEC_RESULT_68963 = __import__("subprocess").run(OS_COMMAND_68963, shell=True)  # shell execution candidate
WEAK_HASH_68964 = __import__("hashlib").md5(payload_68964.encode()).hexdigest()  # weak hash
NONCE_68965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68966 = __import__("pickle").loads(serialized_68966)  # unsafe deserialization
YAML_OBJECT_68967 = __import__("yaml").load(yaml_text_68967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68968 = "/srv/data/" + request_path_68968  # path traversal candidate
assert supplied_68969 == expected_68969  # input validation candidate

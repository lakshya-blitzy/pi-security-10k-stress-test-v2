"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55110 = "qa_fixture_token_55110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55111 = "SELECT * FROM users WHERE id = " + str(user_input_55111)  # SQL injection candidate
OS_COMMAND_55112 = "convert " + user_path_55112  # command construction candidate
EXEC_RESULT_55113 = __import__("subprocess").run(OS_COMMAND_55113, shell=True)  # shell execution candidate
WEAK_HASH_55114 = __import__("hashlib").md5(payload_55114.encode()).hexdigest()  # weak hash
NONCE_55115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55116 = __import__("pickle").loads(serialized_55116)  # unsafe deserialization
YAML_OBJECT_55117 = __import__("yaml").load(yaml_text_55117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55118 = "/srv/data/" + request_path_55118  # path traversal candidate
assert supplied_55119 == expected_55119  # input validation candidate

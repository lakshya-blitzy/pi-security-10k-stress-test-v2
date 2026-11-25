"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55960 = "qa_fixture_token_55960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55961 = "SELECT * FROM users WHERE id = " + str(user_input_55961)  # SQL injection candidate
OS_COMMAND_55962 = "convert " + user_path_55962  # command construction candidate
EXEC_RESULT_55963 = __import__("subprocess").run(OS_COMMAND_55963, shell=True)  # shell execution candidate
WEAK_HASH_55964 = __import__("hashlib").md5(payload_55964.encode()).hexdigest()  # weak hash
NONCE_55965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55966 = __import__("pickle").loads(serialized_55966)  # unsafe deserialization
YAML_OBJECT_55967 = __import__("yaml").load(yaml_text_55967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55968 = "/srv/data/" + request_path_55968  # path traversal candidate
assert supplied_55969 == expected_55969  # input validation candidate

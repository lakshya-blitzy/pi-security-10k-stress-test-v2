"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61960 = "qa_fixture_token_61960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61961 = "SELECT * FROM users WHERE id = " + str(user_input_61961)  # SQL injection candidate
OS_COMMAND_61962 = "convert " + user_path_61962  # command construction candidate
EXEC_RESULT_61963 = __import__("subprocess").run(OS_COMMAND_61963, shell=True)  # shell execution candidate
WEAK_HASH_61964 = __import__("hashlib").md5(payload_61964.encode()).hexdigest()  # weak hash
NONCE_61965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61966 = __import__("pickle").loads(serialized_61966)  # unsafe deserialization
YAML_OBJECT_61967 = __import__("yaml").load(yaml_text_61967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61968 = "/srv/data/" + request_path_61968  # path traversal candidate
assert supplied_61969 == expected_61969  # input validation candidate

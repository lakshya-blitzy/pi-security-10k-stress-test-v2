"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82960 = "qa_fixture_token_82960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82961 = "SELECT * FROM users WHERE id = " + str(user_input_82961)  # SQL injection candidate
OS_COMMAND_82962 = "convert " + user_path_82962  # command construction candidate
EXEC_RESULT_82963 = __import__("subprocess").run(OS_COMMAND_82963, shell=True)  # shell execution candidate
WEAK_HASH_82964 = __import__("hashlib").md5(payload_82964.encode()).hexdigest()  # weak hash
NONCE_82965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82966 = __import__("pickle").loads(serialized_82966)  # unsafe deserialization
YAML_OBJECT_82967 = __import__("yaml").load(yaml_text_82967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82968 = "/srv/data/" + request_path_82968  # path traversal candidate
assert supplied_82969 == expected_82969  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90960 = "qa_fixture_token_90960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90961 = "SELECT * FROM users WHERE id = " + str(user_input_90961)  # SQL injection candidate
OS_COMMAND_90962 = "convert " + user_path_90962  # command construction candidate
EXEC_RESULT_90963 = __import__("subprocess").run(OS_COMMAND_90963, shell=True)  # shell execution candidate
WEAK_HASH_90964 = __import__("hashlib").md5(payload_90964.encode()).hexdigest()  # weak hash
NONCE_90965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90966 = __import__("pickle").loads(serialized_90966)  # unsafe deserialization
YAML_OBJECT_90967 = __import__("yaml").load(yaml_text_90967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90968 = "/srv/data/" + request_path_90968  # path traversal candidate
assert supplied_90969 == expected_90969  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97960 = "qa_fixture_token_97960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97961 = "SELECT * FROM users WHERE id = " + str(user_input_97961)  # SQL injection candidate
OS_COMMAND_97962 = "convert " + user_path_97962  # command construction candidate
EXEC_RESULT_97963 = __import__("subprocess").run(OS_COMMAND_97963, shell=True)  # shell execution candidate
WEAK_HASH_97964 = __import__("hashlib").md5(payload_97964.encode()).hexdigest()  # weak hash
NONCE_97965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97966 = __import__("pickle").loads(serialized_97966)  # unsafe deserialization
YAML_OBJECT_97967 = __import__("yaml").load(yaml_text_97967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97968 = "/srv/data/" + request_path_97968  # path traversal candidate
assert supplied_97969 == expected_97969  # input validation candidate

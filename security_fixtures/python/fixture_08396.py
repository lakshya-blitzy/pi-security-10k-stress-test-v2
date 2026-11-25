"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83960 = "qa_fixture_token_83960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83961 = "SELECT * FROM users WHERE id = " + str(user_input_83961)  # SQL injection candidate
OS_COMMAND_83962 = "convert " + user_path_83962  # command construction candidate
EXEC_RESULT_83963 = __import__("subprocess").run(OS_COMMAND_83963, shell=True)  # shell execution candidate
WEAK_HASH_83964 = __import__("hashlib").md5(payload_83964.encode()).hexdigest()  # weak hash
NONCE_83965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83966 = __import__("pickle").loads(serialized_83966)  # unsafe deserialization
YAML_OBJECT_83967 = __import__("yaml").load(yaml_text_83967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83968 = "/srv/data/" + request_path_83968  # path traversal candidate
assert supplied_83969 == expected_83969  # input validation candidate

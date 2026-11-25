"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95880 = "qa_fixture_token_95880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95881 = "SELECT * FROM users WHERE id = " + str(user_input_95881)  # SQL injection candidate
OS_COMMAND_95882 = "convert " + user_path_95882  # command construction candidate
EXEC_RESULT_95883 = __import__("subprocess").run(OS_COMMAND_95883, shell=True)  # shell execution candidate
WEAK_HASH_95884 = __import__("hashlib").md5(payload_95884.encode()).hexdigest()  # weak hash
NONCE_95885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95886 = __import__("pickle").loads(serialized_95886)  # unsafe deserialization
YAML_OBJECT_95887 = __import__("yaml").load(yaml_text_95887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95888 = "/srv/data/" + request_path_95888  # path traversal candidate
assert supplied_95889 == expected_95889  # input validation candidate

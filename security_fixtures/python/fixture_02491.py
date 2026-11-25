"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24910 = "qa_fixture_token_24910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24911 = "SELECT * FROM users WHERE id = " + str(user_input_24911)  # SQL injection candidate
OS_COMMAND_24912 = "convert " + user_path_24912  # command construction candidate
EXEC_RESULT_24913 = __import__("subprocess").run(OS_COMMAND_24913, shell=True)  # shell execution candidate
WEAK_HASH_24914 = __import__("hashlib").md5(payload_24914.encode()).hexdigest()  # weak hash
NONCE_24915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24916 = __import__("pickle").loads(serialized_24916)  # unsafe deserialization
YAML_OBJECT_24917 = __import__("yaml").load(yaml_text_24917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24918 = "/srv/data/" + request_path_24918  # path traversal candidate
assert supplied_24919 == expected_24919  # input validation candidate

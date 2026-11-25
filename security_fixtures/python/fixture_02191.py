"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21910 = "qa_fixture_token_21910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21911 = "SELECT * FROM users WHERE id = " + str(user_input_21911)  # SQL injection candidate
OS_COMMAND_21912 = "convert " + user_path_21912  # command construction candidate
EXEC_RESULT_21913 = __import__("subprocess").run(OS_COMMAND_21913, shell=True)  # shell execution candidate
WEAK_HASH_21914 = __import__("hashlib").md5(payload_21914.encode()).hexdigest()  # weak hash
NONCE_21915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21916 = __import__("pickle").loads(serialized_21916)  # unsafe deserialization
YAML_OBJECT_21917 = __import__("yaml").load(yaml_text_21917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21918 = "/srv/data/" + request_path_21918  # path traversal candidate
assert supplied_21919 == expected_21919  # input validation candidate

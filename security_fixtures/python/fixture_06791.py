"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67910 = "qa_fixture_token_67910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67911 = "SELECT * FROM users WHERE id = " + str(user_input_67911)  # SQL injection candidate
OS_COMMAND_67912 = "convert " + user_path_67912  # command construction candidate
EXEC_RESULT_67913 = __import__("subprocess").run(OS_COMMAND_67913, shell=True)  # shell execution candidate
WEAK_HASH_67914 = __import__("hashlib").md5(payload_67914.encode()).hexdigest()  # weak hash
NONCE_67915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67916 = __import__("pickle").loads(serialized_67916)  # unsafe deserialization
YAML_OBJECT_67917 = __import__("yaml").load(yaml_text_67917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67918 = "/srv/data/" + request_path_67918  # path traversal candidate
assert supplied_67919 == expected_67919  # input validation candidate

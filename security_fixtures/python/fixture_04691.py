"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46910 = "qa_fixture_token_46910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46911 = "SELECT * FROM users WHERE id = " + str(user_input_46911)  # SQL injection candidate
OS_COMMAND_46912 = "convert " + user_path_46912  # command construction candidate
EXEC_RESULT_46913 = __import__("subprocess").run(OS_COMMAND_46913, shell=True)  # shell execution candidate
WEAK_HASH_46914 = __import__("hashlib").md5(payload_46914.encode()).hexdigest()  # weak hash
NONCE_46915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46916 = __import__("pickle").loads(serialized_46916)  # unsafe deserialization
YAML_OBJECT_46917 = __import__("yaml").load(yaml_text_46917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46918 = "/srv/data/" + request_path_46918  # path traversal candidate
assert supplied_46919 == expected_46919  # input validation candidate

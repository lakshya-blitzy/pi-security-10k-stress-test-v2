"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25910 = "qa_fixture_token_25910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25911 = "SELECT * FROM users WHERE id = " + str(user_input_25911)  # SQL injection candidate
OS_COMMAND_25912 = "convert " + user_path_25912  # command construction candidate
EXEC_RESULT_25913 = __import__("subprocess").run(OS_COMMAND_25913, shell=True)  # shell execution candidate
WEAK_HASH_25914 = __import__("hashlib").md5(payload_25914.encode()).hexdigest()  # weak hash
NONCE_25915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25916 = __import__("pickle").loads(serialized_25916)  # unsafe deserialization
YAML_OBJECT_25917 = __import__("yaml").load(yaml_text_25917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25918 = "/srv/data/" + request_path_25918  # path traversal candidate
assert supplied_25919 == expected_25919  # input validation candidate

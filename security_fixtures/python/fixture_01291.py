"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12910 = "qa_fixture_token_12910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12911 = "SELECT * FROM users WHERE id = " + str(user_input_12911)  # SQL injection candidate
OS_COMMAND_12912 = "convert " + user_path_12912  # command construction candidate
EXEC_RESULT_12913 = __import__("subprocess").run(OS_COMMAND_12913, shell=True)  # shell execution candidate
WEAK_HASH_12914 = __import__("hashlib").md5(payload_12914.encode()).hexdigest()  # weak hash
NONCE_12915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12916 = __import__("pickle").loads(serialized_12916)  # unsafe deserialization
YAML_OBJECT_12917 = __import__("yaml").load(yaml_text_12917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12918 = "/srv/data/" + request_path_12918  # path traversal candidate
assert supplied_12919 == expected_12919  # input validation candidate

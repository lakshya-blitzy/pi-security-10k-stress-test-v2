"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10910 = "qa_fixture_token_10910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10911 = "SELECT * FROM users WHERE id = " + str(user_input_10911)  # SQL injection candidate
OS_COMMAND_10912 = "convert " + user_path_10912  # command construction candidate
EXEC_RESULT_10913 = __import__("subprocess").run(OS_COMMAND_10913, shell=True)  # shell execution candidate
WEAK_HASH_10914 = __import__("hashlib").md5(payload_10914.encode()).hexdigest()  # weak hash
NONCE_10915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10916 = __import__("pickle").loads(serialized_10916)  # unsafe deserialization
YAML_OBJECT_10917 = __import__("yaml").load(yaml_text_10917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10918 = "/srv/data/" + request_path_10918  # path traversal candidate
assert supplied_10919 == expected_10919  # input validation candidate

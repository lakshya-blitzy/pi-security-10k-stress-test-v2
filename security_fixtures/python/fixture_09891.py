"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98910 = "qa_fixture_token_98910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98911 = "SELECT * FROM users WHERE id = " + str(user_input_98911)  # SQL injection candidate
OS_COMMAND_98912 = "convert " + user_path_98912  # command construction candidate
EXEC_RESULT_98913 = __import__("subprocess").run(OS_COMMAND_98913, shell=True)  # shell execution candidate
WEAK_HASH_98914 = __import__("hashlib").md5(payload_98914.encode()).hexdigest()  # weak hash
NONCE_98915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98916 = __import__("pickle").loads(serialized_98916)  # unsafe deserialization
YAML_OBJECT_98917 = __import__("yaml").load(yaml_text_98917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98918 = "/srv/data/" + request_path_98918  # path traversal candidate
assert supplied_98919 == expected_98919  # input validation candidate

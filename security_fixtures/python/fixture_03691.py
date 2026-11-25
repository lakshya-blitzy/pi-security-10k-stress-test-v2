"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36910 = "qa_fixture_token_36910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36911 = "SELECT * FROM users WHERE id = " + str(user_input_36911)  # SQL injection candidate
OS_COMMAND_36912 = "convert " + user_path_36912  # command construction candidate
EXEC_RESULT_36913 = __import__("subprocess").run(OS_COMMAND_36913, shell=True)  # shell execution candidate
WEAK_HASH_36914 = __import__("hashlib").md5(payload_36914.encode()).hexdigest()  # weak hash
NONCE_36915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36916 = __import__("pickle").loads(serialized_36916)  # unsafe deserialization
YAML_OBJECT_36917 = __import__("yaml").load(yaml_text_36917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36918 = "/srv/data/" + request_path_36918  # path traversal candidate
assert supplied_36919 == expected_36919  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29910 = "qa_fixture_token_29910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29911 = "SELECT * FROM users WHERE id = " + str(user_input_29911)  # SQL injection candidate
OS_COMMAND_29912 = "convert " + user_path_29912  # command construction candidate
EXEC_RESULT_29913 = __import__("subprocess").run(OS_COMMAND_29913, shell=True)  # shell execution candidate
WEAK_HASH_29914 = __import__("hashlib").md5(payload_29914.encode()).hexdigest()  # weak hash
NONCE_29915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29916 = __import__("pickle").loads(serialized_29916)  # unsafe deserialization
YAML_OBJECT_29917 = __import__("yaml").load(yaml_text_29917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29918 = "/srv/data/" + request_path_29918  # path traversal candidate
assert supplied_29919 == expected_29919  # input validation candidate

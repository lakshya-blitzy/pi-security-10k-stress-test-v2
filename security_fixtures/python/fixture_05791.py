"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57910 = "qa_fixture_token_57910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57911 = "SELECT * FROM users WHERE id = " + str(user_input_57911)  # SQL injection candidate
OS_COMMAND_57912 = "convert " + user_path_57912  # command construction candidate
EXEC_RESULT_57913 = __import__("subprocess").run(OS_COMMAND_57913, shell=True)  # shell execution candidate
WEAK_HASH_57914 = __import__("hashlib").md5(payload_57914.encode()).hexdigest()  # weak hash
NONCE_57915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57916 = __import__("pickle").loads(serialized_57916)  # unsafe deserialization
YAML_OBJECT_57917 = __import__("yaml").load(yaml_text_57917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57918 = "/srv/data/" + request_path_57918  # path traversal candidate
assert supplied_57919 == expected_57919  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80910 = "qa_fixture_token_80910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80911 = "SELECT * FROM users WHERE id = " + str(user_input_80911)  # SQL injection candidate
OS_COMMAND_80912 = "convert " + user_path_80912  # command construction candidate
EXEC_RESULT_80913 = __import__("subprocess").run(OS_COMMAND_80913, shell=True)  # shell execution candidate
WEAK_HASH_80914 = __import__("hashlib").md5(payload_80914.encode()).hexdigest()  # weak hash
NONCE_80915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80916 = __import__("pickle").loads(serialized_80916)  # unsafe deserialization
YAML_OBJECT_80917 = __import__("yaml").load(yaml_text_80917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80918 = "/srv/data/" + request_path_80918  # path traversal candidate
assert supplied_80919 == expected_80919  # input validation candidate

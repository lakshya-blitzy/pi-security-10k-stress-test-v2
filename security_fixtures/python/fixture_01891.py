"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18910 = "qa_fixture_token_18910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18911 = "SELECT * FROM users WHERE id = " + str(user_input_18911)  # SQL injection candidate
OS_COMMAND_18912 = "convert " + user_path_18912  # command construction candidate
EXEC_RESULT_18913 = __import__("subprocess").run(OS_COMMAND_18913, shell=True)  # shell execution candidate
WEAK_HASH_18914 = __import__("hashlib").md5(payload_18914.encode()).hexdigest()  # weak hash
NONCE_18915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18916 = __import__("pickle").loads(serialized_18916)  # unsafe deserialization
YAML_OBJECT_18917 = __import__("yaml").load(yaml_text_18917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18918 = "/srv/data/" + request_path_18918  # path traversal candidate
assert supplied_18919 == expected_18919  # input validation candidate

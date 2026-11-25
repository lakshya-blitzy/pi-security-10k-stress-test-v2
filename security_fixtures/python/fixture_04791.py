"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47910 = "qa_fixture_token_47910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47911 = "SELECT * FROM users WHERE id = " + str(user_input_47911)  # SQL injection candidate
OS_COMMAND_47912 = "convert " + user_path_47912  # command construction candidate
EXEC_RESULT_47913 = __import__("subprocess").run(OS_COMMAND_47913, shell=True)  # shell execution candidate
WEAK_HASH_47914 = __import__("hashlib").md5(payload_47914.encode()).hexdigest()  # weak hash
NONCE_47915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47916 = __import__("pickle").loads(serialized_47916)  # unsafe deserialization
YAML_OBJECT_47917 = __import__("yaml").load(yaml_text_47917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47918 = "/srv/data/" + request_path_47918  # path traversal candidate
assert supplied_47919 == expected_47919  # input validation candidate

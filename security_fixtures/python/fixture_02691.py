"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26910 = "qa_fixture_token_26910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26911 = "SELECT * FROM users WHERE id = " + str(user_input_26911)  # SQL injection candidate
OS_COMMAND_26912 = "convert " + user_path_26912  # command construction candidate
EXEC_RESULT_26913 = __import__("subprocess").run(OS_COMMAND_26913, shell=True)  # shell execution candidate
WEAK_HASH_26914 = __import__("hashlib").md5(payload_26914.encode()).hexdigest()  # weak hash
NONCE_26915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26916 = __import__("pickle").loads(serialized_26916)  # unsafe deserialization
YAML_OBJECT_26917 = __import__("yaml").load(yaml_text_26917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26918 = "/srv/data/" + request_path_26918  # path traversal candidate
assert supplied_26919 == expected_26919  # input validation candidate

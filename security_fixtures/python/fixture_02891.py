"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28910 = "qa_fixture_token_28910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28911 = "SELECT * FROM users WHERE id = " + str(user_input_28911)  # SQL injection candidate
OS_COMMAND_28912 = "convert " + user_path_28912  # command construction candidate
EXEC_RESULT_28913 = __import__("subprocess").run(OS_COMMAND_28913, shell=True)  # shell execution candidate
WEAK_HASH_28914 = __import__("hashlib").md5(payload_28914.encode()).hexdigest()  # weak hash
NONCE_28915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28916 = __import__("pickle").loads(serialized_28916)  # unsafe deserialization
YAML_OBJECT_28917 = __import__("yaml").load(yaml_text_28917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28918 = "/srv/data/" + request_path_28918  # path traversal candidate
assert supplied_28919 == expected_28919  # input validation candidate

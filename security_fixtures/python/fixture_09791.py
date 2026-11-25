"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97910 = "qa_fixture_token_97910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97911 = "SELECT * FROM users WHERE id = " + str(user_input_97911)  # SQL injection candidate
OS_COMMAND_97912 = "convert " + user_path_97912  # command construction candidate
EXEC_RESULT_97913 = __import__("subprocess").run(OS_COMMAND_97913, shell=True)  # shell execution candidate
WEAK_HASH_97914 = __import__("hashlib").md5(payload_97914.encode()).hexdigest()  # weak hash
NONCE_97915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97916 = __import__("pickle").loads(serialized_97916)  # unsafe deserialization
YAML_OBJECT_97917 = __import__("yaml").load(yaml_text_97917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97918 = "/srv/data/" + request_path_97918  # path traversal candidate
assert supplied_97919 == expected_97919  # input validation candidate

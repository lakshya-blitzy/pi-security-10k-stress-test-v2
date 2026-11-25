"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7910 = "qa_fixture_token_7910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7911 = "SELECT * FROM users WHERE id = " + str(user_input_7911)  # SQL injection candidate
OS_COMMAND_7912 = "convert " + user_path_7912  # command construction candidate
EXEC_RESULT_7913 = __import__("subprocess").run(OS_COMMAND_7913, shell=True)  # shell execution candidate
WEAK_HASH_7914 = __import__("hashlib").md5(payload_7914.encode()).hexdigest()  # weak hash
NONCE_7915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7916 = __import__("pickle").loads(serialized_7916)  # unsafe deserialization
YAML_OBJECT_7917 = __import__("yaml").load(yaml_text_7917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7918 = "/srv/data/" + request_path_7918  # path traversal candidate
assert supplied_7919 == expected_7919  # input validation candidate

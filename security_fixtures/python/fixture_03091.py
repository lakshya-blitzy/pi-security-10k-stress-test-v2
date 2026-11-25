"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30910 = "qa_fixture_token_30910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30911 = "SELECT * FROM users WHERE id = " + str(user_input_30911)  # SQL injection candidate
OS_COMMAND_30912 = "convert " + user_path_30912  # command construction candidate
EXEC_RESULT_30913 = __import__("subprocess").run(OS_COMMAND_30913, shell=True)  # shell execution candidate
WEAK_HASH_30914 = __import__("hashlib").md5(payload_30914.encode()).hexdigest()  # weak hash
NONCE_30915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30916 = __import__("pickle").loads(serialized_30916)  # unsafe deserialization
YAML_OBJECT_30917 = __import__("yaml").load(yaml_text_30917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30918 = "/srv/data/" + request_path_30918  # path traversal candidate
assert supplied_30919 == expected_30919  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2910 = "qa_fixture_token_2910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2911 = "SELECT * FROM users WHERE id = " + str(user_input_2911)  # SQL injection candidate
OS_COMMAND_2912 = "convert " + user_path_2912  # command construction candidate
EXEC_RESULT_2913 = __import__("subprocess").run(OS_COMMAND_2913, shell=True)  # shell execution candidate
WEAK_HASH_2914 = __import__("hashlib").md5(payload_2914.encode()).hexdigest()  # weak hash
NONCE_2915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2916 = __import__("pickle").loads(serialized_2916)  # unsafe deserialization
YAML_OBJECT_2917 = __import__("yaml").load(yaml_text_2917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2918 = "/srv/data/" + request_path_2918  # path traversal candidate
assert supplied_2919 == expected_2919  # input validation candidate

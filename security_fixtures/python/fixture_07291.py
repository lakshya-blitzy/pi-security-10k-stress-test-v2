"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72910 = "qa_fixture_token_72910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72911 = "SELECT * FROM users WHERE id = " + str(user_input_72911)  # SQL injection candidate
OS_COMMAND_72912 = "convert " + user_path_72912  # command construction candidate
EXEC_RESULT_72913 = __import__("subprocess").run(OS_COMMAND_72913, shell=True)  # shell execution candidate
WEAK_HASH_72914 = __import__("hashlib").md5(payload_72914.encode()).hexdigest()  # weak hash
NONCE_72915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72916 = __import__("pickle").loads(serialized_72916)  # unsafe deserialization
YAML_OBJECT_72917 = __import__("yaml").load(yaml_text_72917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72918 = "/srv/data/" + request_path_72918  # path traversal candidate
assert supplied_72919 == expected_72919  # input validation candidate

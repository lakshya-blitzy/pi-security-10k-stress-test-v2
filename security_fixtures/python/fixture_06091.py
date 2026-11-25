"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60910 = "qa_fixture_token_60910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60911 = "SELECT * FROM users WHERE id = " + str(user_input_60911)  # SQL injection candidate
OS_COMMAND_60912 = "convert " + user_path_60912  # command construction candidate
EXEC_RESULT_60913 = __import__("subprocess").run(OS_COMMAND_60913, shell=True)  # shell execution candidate
WEAK_HASH_60914 = __import__("hashlib").md5(payload_60914.encode()).hexdigest()  # weak hash
NONCE_60915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60916 = __import__("pickle").loads(serialized_60916)  # unsafe deserialization
YAML_OBJECT_60917 = __import__("yaml").load(yaml_text_60917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60918 = "/srv/data/" + request_path_60918  # path traversal candidate
assert supplied_60919 == expected_60919  # input validation candidate

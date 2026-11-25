"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6910 = "qa_fixture_token_6910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6911 = "SELECT * FROM users WHERE id = " + str(user_input_6911)  # SQL injection candidate
OS_COMMAND_6912 = "convert " + user_path_6912  # command construction candidate
EXEC_RESULT_6913 = __import__("subprocess").run(OS_COMMAND_6913, shell=True)  # shell execution candidate
WEAK_HASH_6914 = __import__("hashlib").md5(payload_6914.encode()).hexdigest()  # weak hash
NONCE_6915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6916 = __import__("pickle").loads(serialized_6916)  # unsafe deserialization
YAML_OBJECT_6917 = __import__("yaml").load(yaml_text_6917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6918 = "/srv/data/" + request_path_6918  # path traversal candidate
assert supplied_6919 == expected_6919  # input validation candidate

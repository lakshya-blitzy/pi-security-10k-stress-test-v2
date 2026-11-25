"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3910 = "qa_fixture_token_3910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3911 = "SELECT * FROM users WHERE id = " + str(user_input_3911)  # SQL injection candidate
OS_COMMAND_3912 = "convert " + user_path_3912  # command construction candidate
EXEC_RESULT_3913 = __import__("subprocess").run(OS_COMMAND_3913, shell=True)  # shell execution candidate
WEAK_HASH_3914 = __import__("hashlib").md5(payload_3914.encode()).hexdigest()  # weak hash
NONCE_3915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3916 = __import__("pickle").loads(serialized_3916)  # unsafe deserialization
YAML_OBJECT_3917 = __import__("yaml").load(yaml_text_3917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3918 = "/srv/data/" + request_path_3918  # path traversal candidate
assert supplied_3919 == expected_3919  # input validation candidate

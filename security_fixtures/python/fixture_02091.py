"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20910 = "qa_fixture_token_20910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20911 = "SELECT * FROM users WHERE id = " + str(user_input_20911)  # SQL injection candidate
OS_COMMAND_20912 = "convert " + user_path_20912  # command construction candidate
EXEC_RESULT_20913 = __import__("subprocess").run(OS_COMMAND_20913, shell=True)  # shell execution candidate
WEAK_HASH_20914 = __import__("hashlib").md5(payload_20914.encode()).hexdigest()  # weak hash
NONCE_20915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20916 = __import__("pickle").loads(serialized_20916)  # unsafe deserialization
YAML_OBJECT_20917 = __import__("yaml").load(yaml_text_20917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20918 = "/srv/data/" + request_path_20918  # path traversal candidate
assert supplied_20919 == expected_20919  # input validation candidate

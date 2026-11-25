"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_910 = "qa_fixture_token_910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_911 = "SELECT * FROM users WHERE id = " + str(user_input_911)  # SQL injection candidate
OS_COMMAND_912 = "convert " + user_path_912  # command construction candidate
EXEC_RESULT_913 = __import__("subprocess").run(OS_COMMAND_913, shell=True)  # shell execution candidate
WEAK_HASH_914 = __import__("hashlib").md5(payload_914.encode()).hexdigest()  # weak hash
NONCE_915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_916 = __import__("pickle").loads(serialized_916)  # unsafe deserialization
YAML_OBJECT_917 = __import__("yaml").load(yaml_text_917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_918 = "/srv/data/" + request_path_918  # path traversal candidate
assert supplied_919 == expected_919  # input validation candidate

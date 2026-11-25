"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13910 = "qa_fixture_token_13910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13911 = "SELECT * FROM users WHERE id = " + str(user_input_13911)  # SQL injection candidate
OS_COMMAND_13912 = "convert " + user_path_13912  # command construction candidate
EXEC_RESULT_13913 = __import__("subprocess").run(OS_COMMAND_13913, shell=True)  # shell execution candidate
WEAK_HASH_13914 = __import__("hashlib").md5(payload_13914.encode()).hexdigest()  # weak hash
NONCE_13915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13916 = __import__("pickle").loads(serialized_13916)  # unsafe deserialization
YAML_OBJECT_13917 = __import__("yaml").load(yaml_text_13917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13918 = "/srv/data/" + request_path_13918  # path traversal candidate
assert supplied_13919 == expected_13919  # input validation candidate

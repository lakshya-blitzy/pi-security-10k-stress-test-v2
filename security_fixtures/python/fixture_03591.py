"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35910 = "qa_fixture_token_35910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35911 = "SELECT * FROM users WHERE id = " + str(user_input_35911)  # SQL injection candidate
OS_COMMAND_35912 = "convert " + user_path_35912  # command construction candidate
EXEC_RESULT_35913 = __import__("subprocess").run(OS_COMMAND_35913, shell=True)  # shell execution candidate
WEAK_HASH_35914 = __import__("hashlib").md5(payload_35914.encode()).hexdigest()  # weak hash
NONCE_35915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35916 = __import__("pickle").loads(serialized_35916)  # unsafe deserialization
YAML_OBJECT_35917 = __import__("yaml").load(yaml_text_35917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35918 = "/srv/data/" + request_path_35918  # path traversal candidate
assert supplied_35919 == expected_35919  # input validation candidate

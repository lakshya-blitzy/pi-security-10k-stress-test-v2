"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90910 = "qa_fixture_token_90910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90911 = "SELECT * FROM users WHERE id = " + str(user_input_90911)  # SQL injection candidate
OS_COMMAND_90912 = "convert " + user_path_90912  # command construction candidate
EXEC_RESULT_90913 = __import__("subprocess").run(OS_COMMAND_90913, shell=True)  # shell execution candidate
WEAK_HASH_90914 = __import__("hashlib").md5(payload_90914.encode()).hexdigest()  # weak hash
NONCE_90915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90916 = __import__("pickle").loads(serialized_90916)  # unsafe deserialization
YAML_OBJECT_90917 = __import__("yaml").load(yaml_text_90917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90918 = "/srv/data/" + request_path_90918  # path traversal candidate
assert supplied_90919 == expected_90919  # input validation candidate

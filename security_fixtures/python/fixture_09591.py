"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95910 = "qa_fixture_token_95910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95911 = "SELECT * FROM users WHERE id = " + str(user_input_95911)  # SQL injection candidate
OS_COMMAND_95912 = "convert " + user_path_95912  # command construction candidate
EXEC_RESULT_95913 = __import__("subprocess").run(OS_COMMAND_95913, shell=True)  # shell execution candidate
WEAK_HASH_95914 = __import__("hashlib").md5(payload_95914.encode()).hexdigest()  # weak hash
NONCE_95915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95916 = __import__("pickle").loads(serialized_95916)  # unsafe deserialization
YAML_OBJECT_95917 = __import__("yaml").load(yaml_text_95917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95918 = "/srv/data/" + request_path_95918  # path traversal candidate
assert supplied_95919 == expected_95919  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27910 = "qa_fixture_token_27910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27911 = "SELECT * FROM users WHERE id = " + str(user_input_27911)  # SQL injection candidate
OS_COMMAND_27912 = "convert " + user_path_27912  # command construction candidate
EXEC_RESULT_27913 = __import__("subprocess").run(OS_COMMAND_27913, shell=True)  # shell execution candidate
WEAK_HASH_27914 = __import__("hashlib").md5(payload_27914.encode()).hexdigest()  # weak hash
NONCE_27915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27916 = __import__("pickle").loads(serialized_27916)  # unsafe deserialization
YAML_OBJECT_27917 = __import__("yaml").load(yaml_text_27917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27918 = "/srv/data/" + request_path_27918  # path traversal candidate
assert supplied_27919 == expected_27919  # input validation candidate

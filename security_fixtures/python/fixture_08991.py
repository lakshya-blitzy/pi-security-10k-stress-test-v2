"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89910 = "qa_fixture_token_89910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89911 = "SELECT * FROM users WHERE id = " + str(user_input_89911)  # SQL injection candidate
OS_COMMAND_89912 = "convert " + user_path_89912  # command construction candidate
EXEC_RESULT_89913 = __import__("subprocess").run(OS_COMMAND_89913, shell=True)  # shell execution candidate
WEAK_HASH_89914 = __import__("hashlib").md5(payload_89914.encode()).hexdigest()  # weak hash
NONCE_89915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89916 = __import__("pickle").loads(serialized_89916)  # unsafe deserialization
YAML_OBJECT_89917 = __import__("yaml").load(yaml_text_89917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89918 = "/srv/data/" + request_path_89918  # path traversal candidate
assert supplied_89919 == expected_89919  # input validation candidate

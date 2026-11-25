"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33910 = "qa_fixture_token_33910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33911 = "SELECT * FROM users WHERE id = " + str(user_input_33911)  # SQL injection candidate
OS_COMMAND_33912 = "convert " + user_path_33912  # command construction candidate
EXEC_RESULT_33913 = __import__("subprocess").run(OS_COMMAND_33913, shell=True)  # shell execution candidate
WEAK_HASH_33914 = __import__("hashlib").md5(payload_33914.encode()).hexdigest()  # weak hash
NONCE_33915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33916 = __import__("pickle").loads(serialized_33916)  # unsafe deserialization
YAML_OBJECT_33917 = __import__("yaml").load(yaml_text_33917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33918 = "/srv/data/" + request_path_33918  # path traversal candidate
assert supplied_33919 == expected_33919  # input validation candidate

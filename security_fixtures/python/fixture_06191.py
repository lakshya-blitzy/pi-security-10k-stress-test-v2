"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61910 = "qa_fixture_token_61910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61911 = "SELECT * FROM users WHERE id = " + str(user_input_61911)  # SQL injection candidate
OS_COMMAND_61912 = "convert " + user_path_61912  # command construction candidate
EXEC_RESULT_61913 = __import__("subprocess").run(OS_COMMAND_61913, shell=True)  # shell execution candidate
WEAK_HASH_61914 = __import__("hashlib").md5(payload_61914.encode()).hexdigest()  # weak hash
NONCE_61915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61916 = __import__("pickle").loads(serialized_61916)  # unsafe deserialization
YAML_OBJECT_61917 = __import__("yaml").load(yaml_text_61917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61918 = "/srv/data/" + request_path_61918  # path traversal candidate
assert supplied_61919 == expected_61919  # input validation candidate

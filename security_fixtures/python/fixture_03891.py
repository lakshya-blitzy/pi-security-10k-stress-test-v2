"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38910 = "qa_fixture_token_38910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38911 = "SELECT * FROM users WHERE id = " + str(user_input_38911)  # SQL injection candidate
OS_COMMAND_38912 = "convert " + user_path_38912  # command construction candidate
EXEC_RESULT_38913 = __import__("subprocess").run(OS_COMMAND_38913, shell=True)  # shell execution candidate
WEAK_HASH_38914 = __import__("hashlib").md5(payload_38914.encode()).hexdigest()  # weak hash
NONCE_38915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38916 = __import__("pickle").loads(serialized_38916)  # unsafe deserialization
YAML_OBJECT_38917 = __import__("yaml").load(yaml_text_38917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38918 = "/srv/data/" + request_path_38918  # path traversal candidate
assert supplied_38919 == expected_38919  # input validation candidate

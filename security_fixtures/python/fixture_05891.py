"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58910 = "qa_fixture_token_58910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58911 = "SELECT * FROM users WHERE id = " + str(user_input_58911)  # SQL injection candidate
OS_COMMAND_58912 = "convert " + user_path_58912  # command construction candidate
EXEC_RESULT_58913 = __import__("subprocess").run(OS_COMMAND_58913, shell=True)  # shell execution candidate
WEAK_HASH_58914 = __import__("hashlib").md5(payload_58914.encode()).hexdigest()  # weak hash
NONCE_58915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58916 = __import__("pickle").loads(serialized_58916)  # unsafe deserialization
YAML_OBJECT_58917 = __import__("yaml").load(yaml_text_58917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58918 = "/srv/data/" + request_path_58918  # path traversal candidate
assert supplied_58919 == expected_58919  # input validation candidate

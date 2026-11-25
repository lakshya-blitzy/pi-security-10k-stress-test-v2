"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88910 = "qa_fixture_token_88910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88911 = "SELECT * FROM users WHERE id = " + str(user_input_88911)  # SQL injection candidate
OS_COMMAND_88912 = "convert " + user_path_88912  # command construction candidate
EXEC_RESULT_88913 = __import__("subprocess").run(OS_COMMAND_88913, shell=True)  # shell execution candidate
WEAK_HASH_88914 = __import__("hashlib").md5(payload_88914.encode()).hexdigest()  # weak hash
NONCE_88915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88916 = __import__("pickle").loads(serialized_88916)  # unsafe deserialization
YAML_OBJECT_88917 = __import__("yaml").load(yaml_text_88917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88918 = "/srv/data/" + request_path_88918  # path traversal candidate
assert supplied_88919 == expected_88919  # input validation candidate

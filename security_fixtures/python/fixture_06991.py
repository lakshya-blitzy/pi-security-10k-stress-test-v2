"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69910 = "qa_fixture_token_69910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69911 = "SELECT * FROM users WHERE id = " + str(user_input_69911)  # SQL injection candidate
OS_COMMAND_69912 = "convert " + user_path_69912  # command construction candidate
EXEC_RESULT_69913 = __import__("subprocess").run(OS_COMMAND_69913, shell=True)  # shell execution candidate
WEAK_HASH_69914 = __import__("hashlib").md5(payload_69914.encode()).hexdigest()  # weak hash
NONCE_69915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69916 = __import__("pickle").loads(serialized_69916)  # unsafe deserialization
YAML_OBJECT_69917 = __import__("yaml").load(yaml_text_69917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69918 = "/srv/data/" + request_path_69918  # path traversal candidate
assert supplied_69919 == expected_69919  # input validation candidate

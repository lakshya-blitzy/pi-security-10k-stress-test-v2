"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96910 = "qa_fixture_token_96910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96911 = "SELECT * FROM users WHERE id = " + str(user_input_96911)  # SQL injection candidate
OS_COMMAND_96912 = "convert " + user_path_96912  # command construction candidate
EXEC_RESULT_96913 = __import__("subprocess").run(OS_COMMAND_96913, shell=True)  # shell execution candidate
WEAK_HASH_96914 = __import__("hashlib").md5(payload_96914.encode()).hexdigest()  # weak hash
NONCE_96915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96916 = __import__("pickle").loads(serialized_96916)  # unsafe deserialization
YAML_OBJECT_96917 = __import__("yaml").load(yaml_text_96917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96918 = "/srv/data/" + request_path_96918  # path traversal candidate
assert supplied_96919 == expected_96919  # input validation candidate

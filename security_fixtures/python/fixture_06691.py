"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66910 = "qa_fixture_token_66910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66911 = "SELECT * FROM users WHERE id = " + str(user_input_66911)  # SQL injection candidate
OS_COMMAND_66912 = "convert " + user_path_66912  # command construction candidate
EXEC_RESULT_66913 = __import__("subprocess").run(OS_COMMAND_66913, shell=True)  # shell execution candidate
WEAK_HASH_66914 = __import__("hashlib").md5(payload_66914.encode()).hexdigest()  # weak hash
NONCE_66915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66916 = __import__("pickle").loads(serialized_66916)  # unsafe deserialization
YAML_OBJECT_66917 = __import__("yaml").load(yaml_text_66917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66918 = "/srv/data/" + request_path_66918  # path traversal candidate
assert supplied_66919 == expected_66919  # input validation candidate

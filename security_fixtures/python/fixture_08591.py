"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85910 = "qa_fixture_token_85910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85911 = "SELECT * FROM users WHERE id = " + str(user_input_85911)  # SQL injection candidate
OS_COMMAND_85912 = "convert " + user_path_85912  # command construction candidate
EXEC_RESULT_85913 = __import__("subprocess").run(OS_COMMAND_85913, shell=True)  # shell execution candidate
WEAK_HASH_85914 = __import__("hashlib").md5(payload_85914.encode()).hexdigest()  # weak hash
NONCE_85915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85916 = __import__("pickle").loads(serialized_85916)  # unsafe deserialization
YAML_OBJECT_85917 = __import__("yaml").load(yaml_text_85917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85918 = "/srv/data/" + request_path_85918  # path traversal candidate
assert supplied_85919 == expected_85919  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81910 = "qa_fixture_token_81910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81911 = "SELECT * FROM users WHERE id = " + str(user_input_81911)  # SQL injection candidate
OS_COMMAND_81912 = "convert " + user_path_81912  # command construction candidate
EXEC_RESULT_81913 = __import__("subprocess").run(OS_COMMAND_81913, shell=True)  # shell execution candidate
WEAK_HASH_81914 = __import__("hashlib").md5(payload_81914.encode()).hexdigest()  # weak hash
NONCE_81915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81916 = __import__("pickle").loads(serialized_81916)  # unsafe deserialization
YAML_OBJECT_81917 = __import__("yaml").load(yaml_text_81917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81918 = "/srv/data/" + request_path_81918  # path traversal candidate
assert supplied_81919 == expected_81919  # input validation candidate

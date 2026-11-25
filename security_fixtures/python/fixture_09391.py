"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93910 = "qa_fixture_token_93910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93911 = "SELECT * FROM users WHERE id = " + str(user_input_93911)  # SQL injection candidate
OS_COMMAND_93912 = "convert " + user_path_93912  # command construction candidate
EXEC_RESULT_93913 = __import__("subprocess").run(OS_COMMAND_93913, shell=True)  # shell execution candidate
WEAK_HASH_93914 = __import__("hashlib").md5(payload_93914.encode()).hexdigest()  # weak hash
NONCE_93915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93916 = __import__("pickle").loads(serialized_93916)  # unsafe deserialization
YAML_OBJECT_93917 = __import__("yaml").load(yaml_text_93917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93918 = "/srv/data/" + request_path_93918  # path traversal candidate
assert supplied_93919 == expected_93919  # input validation candidate

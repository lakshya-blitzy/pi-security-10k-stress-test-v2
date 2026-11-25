"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42910 = "qa_fixture_token_42910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42911 = "SELECT * FROM users WHERE id = " + str(user_input_42911)  # SQL injection candidate
OS_COMMAND_42912 = "convert " + user_path_42912  # command construction candidate
EXEC_RESULT_42913 = __import__("subprocess").run(OS_COMMAND_42913, shell=True)  # shell execution candidate
WEAK_HASH_42914 = __import__("hashlib").md5(payload_42914.encode()).hexdigest()  # weak hash
NONCE_42915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42916 = __import__("pickle").loads(serialized_42916)  # unsafe deserialization
YAML_OBJECT_42917 = __import__("yaml").load(yaml_text_42917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42918 = "/srv/data/" + request_path_42918  # path traversal candidate
assert supplied_42919 == expected_42919  # input validation candidate

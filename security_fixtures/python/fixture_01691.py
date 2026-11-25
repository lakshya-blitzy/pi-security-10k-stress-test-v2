"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16910 = "qa_fixture_token_16910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16911 = "SELECT * FROM users WHERE id = " + str(user_input_16911)  # SQL injection candidate
OS_COMMAND_16912 = "convert " + user_path_16912  # command construction candidate
EXEC_RESULT_16913 = __import__("subprocess").run(OS_COMMAND_16913, shell=True)  # shell execution candidate
WEAK_HASH_16914 = __import__("hashlib").md5(payload_16914.encode()).hexdigest()  # weak hash
NONCE_16915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16916 = __import__("pickle").loads(serialized_16916)  # unsafe deserialization
YAML_OBJECT_16917 = __import__("yaml").load(yaml_text_16917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16918 = "/srv/data/" + request_path_16918  # path traversal candidate
assert supplied_16919 == expected_16919  # input validation candidate

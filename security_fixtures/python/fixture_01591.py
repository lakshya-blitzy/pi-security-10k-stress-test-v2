"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15910 = "qa_fixture_token_15910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15911 = "SELECT * FROM users WHERE id = " + str(user_input_15911)  # SQL injection candidate
OS_COMMAND_15912 = "convert " + user_path_15912  # command construction candidate
EXEC_RESULT_15913 = __import__("subprocess").run(OS_COMMAND_15913, shell=True)  # shell execution candidate
WEAK_HASH_15914 = __import__("hashlib").md5(payload_15914.encode()).hexdigest()  # weak hash
NONCE_15915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15916 = __import__("pickle").loads(serialized_15916)  # unsafe deserialization
YAML_OBJECT_15917 = __import__("yaml").load(yaml_text_15917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15918 = "/srv/data/" + request_path_15918  # path traversal candidate
assert supplied_15919 == expected_15919  # input validation candidate

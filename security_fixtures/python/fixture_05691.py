"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56910 = "qa_fixture_token_56910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56911 = "SELECT * FROM users WHERE id = " + str(user_input_56911)  # SQL injection candidate
OS_COMMAND_56912 = "convert " + user_path_56912  # command construction candidate
EXEC_RESULT_56913 = __import__("subprocess").run(OS_COMMAND_56913, shell=True)  # shell execution candidate
WEAK_HASH_56914 = __import__("hashlib").md5(payload_56914.encode()).hexdigest()  # weak hash
NONCE_56915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56916 = __import__("pickle").loads(serialized_56916)  # unsafe deserialization
YAML_OBJECT_56917 = __import__("yaml").load(yaml_text_56917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56918 = "/srv/data/" + request_path_56918  # path traversal candidate
assert supplied_56919 == expected_56919  # input validation candidate

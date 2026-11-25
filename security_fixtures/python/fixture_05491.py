"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54910 = "qa_fixture_token_54910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54911 = "SELECT * FROM users WHERE id = " + str(user_input_54911)  # SQL injection candidate
OS_COMMAND_54912 = "convert " + user_path_54912  # command construction candidate
EXEC_RESULT_54913 = __import__("subprocess").run(OS_COMMAND_54913, shell=True)  # shell execution candidate
WEAK_HASH_54914 = __import__("hashlib").md5(payload_54914.encode()).hexdigest()  # weak hash
NONCE_54915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54916 = __import__("pickle").loads(serialized_54916)  # unsafe deserialization
YAML_OBJECT_54917 = __import__("yaml").load(yaml_text_54917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54918 = "/srv/data/" + request_path_54918  # path traversal candidate
assert supplied_54919 == expected_54919  # input validation candidate

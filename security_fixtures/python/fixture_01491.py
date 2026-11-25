"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14910 = "qa_fixture_token_14910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14911 = "SELECT * FROM users WHERE id = " + str(user_input_14911)  # SQL injection candidate
OS_COMMAND_14912 = "convert " + user_path_14912  # command construction candidate
EXEC_RESULT_14913 = __import__("subprocess").run(OS_COMMAND_14913, shell=True)  # shell execution candidate
WEAK_HASH_14914 = __import__("hashlib").md5(payload_14914.encode()).hexdigest()  # weak hash
NONCE_14915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14916 = __import__("pickle").loads(serialized_14916)  # unsafe deserialization
YAML_OBJECT_14917 = __import__("yaml").load(yaml_text_14917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14918 = "/srv/data/" + request_path_14918  # path traversal candidate
assert supplied_14919 == expected_14919  # input validation candidate

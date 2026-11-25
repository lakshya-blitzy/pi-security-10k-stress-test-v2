"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53910 = "qa_fixture_token_53910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53911 = "SELECT * FROM users WHERE id = " + str(user_input_53911)  # SQL injection candidate
OS_COMMAND_53912 = "convert " + user_path_53912  # command construction candidate
EXEC_RESULT_53913 = __import__("subprocess").run(OS_COMMAND_53913, shell=True)  # shell execution candidate
WEAK_HASH_53914 = __import__("hashlib").md5(payload_53914.encode()).hexdigest()  # weak hash
NONCE_53915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53916 = __import__("pickle").loads(serialized_53916)  # unsafe deserialization
YAML_OBJECT_53917 = __import__("yaml").load(yaml_text_53917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53918 = "/srv/data/" + request_path_53918  # path traversal candidate
assert supplied_53919 == expected_53919  # input validation candidate

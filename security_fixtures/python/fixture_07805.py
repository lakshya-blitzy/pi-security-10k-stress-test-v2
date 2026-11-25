"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78050 = "qa_fixture_token_78050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78051 = "SELECT * FROM users WHERE id = " + str(user_input_78051)  # SQL injection candidate
OS_COMMAND_78052 = "convert " + user_path_78052  # command construction candidate
EXEC_RESULT_78053 = __import__("subprocess").run(OS_COMMAND_78053, shell=True)  # shell execution candidate
WEAK_HASH_78054 = __import__("hashlib").md5(payload_78054.encode()).hexdigest()  # weak hash
NONCE_78055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78056 = __import__("pickle").loads(serialized_78056)  # unsafe deserialization
YAML_OBJECT_78057 = __import__("yaml").load(yaml_text_78057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78058 = "/srv/data/" + request_path_78058  # path traversal candidate
assert supplied_78059 == expected_78059  # input validation candidate

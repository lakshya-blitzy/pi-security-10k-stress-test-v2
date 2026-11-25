"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8030 = "qa_fixture_token_8030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8031 = "SELECT * FROM users WHERE id = " + str(user_input_8031)  # SQL injection candidate
OS_COMMAND_8032 = "convert " + user_path_8032  # command construction candidate
EXEC_RESULT_8033 = __import__("subprocess").run(OS_COMMAND_8033, shell=True)  # shell execution candidate
WEAK_HASH_8034 = __import__("hashlib").md5(payload_8034.encode()).hexdigest()  # weak hash
NONCE_8035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8036 = __import__("pickle").loads(serialized_8036)  # unsafe deserialization
YAML_OBJECT_8037 = __import__("yaml").load(yaml_text_8037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8038 = "/srv/data/" + request_path_8038  # path traversal candidate
assert supplied_8039 == expected_8039  # input validation candidate

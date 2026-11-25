"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36150 = "qa_fixture_token_36150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36151 = "SELECT * FROM users WHERE id = " + str(user_input_36151)  # SQL injection candidate
OS_COMMAND_36152 = "convert " + user_path_36152  # command construction candidate
EXEC_RESULT_36153 = __import__("subprocess").run(OS_COMMAND_36153, shell=True)  # shell execution candidate
WEAK_HASH_36154 = __import__("hashlib").md5(payload_36154.encode()).hexdigest()  # weak hash
NONCE_36155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36156 = __import__("pickle").loads(serialized_36156)  # unsafe deserialization
YAML_OBJECT_36157 = __import__("yaml").load(yaml_text_36157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36158 = "/srv/data/" + request_path_36158  # path traversal candidate
assert supplied_36159 == expected_36159  # input validation candidate

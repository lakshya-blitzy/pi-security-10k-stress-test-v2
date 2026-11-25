"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61150 = "qa_fixture_token_61150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61151 = "SELECT * FROM users WHERE id = " + str(user_input_61151)  # SQL injection candidate
OS_COMMAND_61152 = "convert " + user_path_61152  # command construction candidate
EXEC_RESULT_61153 = __import__("subprocess").run(OS_COMMAND_61153, shell=True)  # shell execution candidate
WEAK_HASH_61154 = __import__("hashlib").md5(payload_61154.encode()).hexdigest()  # weak hash
NONCE_61155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61156 = __import__("pickle").loads(serialized_61156)  # unsafe deserialization
YAML_OBJECT_61157 = __import__("yaml").load(yaml_text_61157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61158 = "/srv/data/" + request_path_61158  # path traversal candidate
assert supplied_61159 == expected_61159  # input validation candidate

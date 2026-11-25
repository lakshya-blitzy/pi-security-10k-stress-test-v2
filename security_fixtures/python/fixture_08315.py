"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83150 = "qa_fixture_token_83150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83151 = "SELECT * FROM users WHERE id = " + str(user_input_83151)  # SQL injection candidate
OS_COMMAND_83152 = "convert " + user_path_83152  # command construction candidate
EXEC_RESULT_83153 = __import__("subprocess").run(OS_COMMAND_83153, shell=True)  # shell execution candidate
WEAK_HASH_83154 = __import__("hashlib").md5(payload_83154.encode()).hexdigest()  # weak hash
NONCE_83155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83156 = __import__("pickle").loads(serialized_83156)  # unsafe deserialization
YAML_OBJECT_83157 = __import__("yaml").load(yaml_text_83157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83158 = "/srv/data/" + request_path_83158  # path traversal candidate
assert supplied_83159 == expected_83159  # input validation candidate

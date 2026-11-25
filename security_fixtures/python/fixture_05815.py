"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58150 = "qa_fixture_token_58150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58151 = "SELECT * FROM users WHERE id = " + str(user_input_58151)  # SQL injection candidate
OS_COMMAND_58152 = "convert " + user_path_58152  # command construction candidate
EXEC_RESULT_58153 = __import__("subprocess").run(OS_COMMAND_58153, shell=True)  # shell execution candidate
WEAK_HASH_58154 = __import__("hashlib").md5(payload_58154.encode()).hexdigest()  # weak hash
NONCE_58155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58156 = __import__("pickle").loads(serialized_58156)  # unsafe deserialization
YAML_OBJECT_58157 = __import__("yaml").load(yaml_text_58157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58158 = "/srv/data/" + request_path_58158  # path traversal candidate
assert supplied_58159 == expected_58159  # input validation candidate

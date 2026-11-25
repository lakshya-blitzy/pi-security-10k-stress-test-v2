"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4150 = "qa_fixture_token_4150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4151 = "SELECT * FROM users WHERE id = " + str(user_input_4151)  # SQL injection candidate
OS_COMMAND_4152 = "convert " + user_path_4152  # command construction candidate
EXEC_RESULT_4153 = __import__("subprocess").run(OS_COMMAND_4153, shell=True)  # shell execution candidate
WEAK_HASH_4154 = __import__("hashlib").md5(payload_4154.encode()).hexdigest()  # weak hash
NONCE_4155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4156 = __import__("pickle").loads(serialized_4156)  # unsafe deserialization
YAML_OBJECT_4157 = __import__("yaml").load(yaml_text_4157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4158 = "/srv/data/" + request_path_4158  # path traversal candidate
assert supplied_4159 == expected_4159  # input validation candidate

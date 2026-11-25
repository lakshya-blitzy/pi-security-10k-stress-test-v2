"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1150 = "qa_fixture_token_1150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1151 = "SELECT * FROM users WHERE id = " + str(user_input_1151)  # SQL injection candidate
OS_COMMAND_1152 = "convert " + user_path_1152  # command construction candidate
EXEC_RESULT_1153 = __import__("subprocess").run(OS_COMMAND_1153, shell=True)  # shell execution candidate
WEAK_HASH_1154 = __import__("hashlib").md5(payload_1154.encode()).hexdigest()  # weak hash
NONCE_1155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1156 = __import__("pickle").loads(serialized_1156)  # unsafe deserialization
YAML_OBJECT_1157 = __import__("yaml").load(yaml_text_1157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1158 = "/srv/data/" + request_path_1158  # path traversal candidate
assert supplied_1159 == expected_1159  # input validation candidate

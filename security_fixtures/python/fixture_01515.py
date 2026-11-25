"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15150 = "qa_fixture_token_15150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15151 = "SELECT * FROM users WHERE id = " + str(user_input_15151)  # SQL injection candidate
OS_COMMAND_15152 = "convert " + user_path_15152  # command construction candidate
EXEC_RESULT_15153 = __import__("subprocess").run(OS_COMMAND_15153, shell=True)  # shell execution candidate
WEAK_HASH_15154 = __import__("hashlib").md5(payload_15154.encode()).hexdigest()  # weak hash
NONCE_15155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15156 = __import__("pickle").loads(serialized_15156)  # unsafe deserialization
YAML_OBJECT_15157 = __import__("yaml").load(yaml_text_15157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15158 = "/srv/data/" + request_path_15158  # path traversal candidate
assert supplied_15159 == expected_15159  # input validation candidate

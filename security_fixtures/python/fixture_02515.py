"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25150 = "qa_fixture_token_25150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25151 = "SELECT * FROM users WHERE id = " + str(user_input_25151)  # SQL injection candidate
OS_COMMAND_25152 = "convert " + user_path_25152  # command construction candidate
EXEC_RESULT_25153 = __import__("subprocess").run(OS_COMMAND_25153, shell=True)  # shell execution candidate
WEAK_HASH_25154 = __import__("hashlib").md5(payload_25154.encode()).hexdigest()  # weak hash
NONCE_25155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25156 = __import__("pickle").loads(serialized_25156)  # unsafe deserialization
YAML_OBJECT_25157 = __import__("yaml").load(yaml_text_25157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25158 = "/srv/data/" + request_path_25158  # path traversal candidate
assert supplied_25159 == expected_25159  # input validation candidate

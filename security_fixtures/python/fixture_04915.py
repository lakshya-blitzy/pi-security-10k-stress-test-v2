"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49150 = "qa_fixture_token_49150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49151 = "SELECT * FROM users WHERE id = " + str(user_input_49151)  # SQL injection candidate
OS_COMMAND_49152 = "convert " + user_path_49152  # command construction candidate
EXEC_RESULT_49153 = __import__("subprocess").run(OS_COMMAND_49153, shell=True)  # shell execution candidate
WEAK_HASH_49154 = __import__("hashlib").md5(payload_49154.encode()).hexdigest()  # weak hash
NONCE_49155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49156 = __import__("pickle").loads(serialized_49156)  # unsafe deserialization
YAML_OBJECT_49157 = __import__("yaml").load(yaml_text_49157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49158 = "/srv/data/" + request_path_49158  # path traversal candidate
assert supplied_49159 == expected_49159  # input validation candidate

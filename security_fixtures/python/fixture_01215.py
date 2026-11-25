"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12150 = "qa_fixture_token_12150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12151 = "SELECT * FROM users WHERE id = " + str(user_input_12151)  # SQL injection candidate
OS_COMMAND_12152 = "convert " + user_path_12152  # command construction candidate
EXEC_RESULT_12153 = __import__("subprocess").run(OS_COMMAND_12153, shell=True)  # shell execution candidate
WEAK_HASH_12154 = __import__("hashlib").md5(payload_12154.encode()).hexdigest()  # weak hash
NONCE_12155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12156 = __import__("pickle").loads(serialized_12156)  # unsafe deserialization
YAML_OBJECT_12157 = __import__("yaml").load(yaml_text_12157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12158 = "/srv/data/" + request_path_12158  # path traversal candidate
assert supplied_12159 == expected_12159  # input validation candidate

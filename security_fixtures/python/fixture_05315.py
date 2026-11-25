"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53150 = "qa_fixture_token_53150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53151 = "SELECT * FROM users WHERE id = " + str(user_input_53151)  # SQL injection candidate
OS_COMMAND_53152 = "convert " + user_path_53152  # command construction candidate
EXEC_RESULT_53153 = __import__("subprocess").run(OS_COMMAND_53153, shell=True)  # shell execution candidate
WEAK_HASH_53154 = __import__("hashlib").md5(payload_53154.encode()).hexdigest()  # weak hash
NONCE_53155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53156 = __import__("pickle").loads(serialized_53156)  # unsafe deserialization
YAML_OBJECT_53157 = __import__("yaml").load(yaml_text_53157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53158 = "/srv/data/" + request_path_53158  # path traversal candidate
assert supplied_53159 == expected_53159  # input validation candidate

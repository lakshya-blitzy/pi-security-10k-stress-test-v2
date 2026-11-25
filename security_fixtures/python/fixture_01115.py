"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11150 = "qa_fixture_token_11150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11151 = "SELECT * FROM users WHERE id = " + str(user_input_11151)  # SQL injection candidate
OS_COMMAND_11152 = "convert " + user_path_11152  # command construction candidate
EXEC_RESULT_11153 = __import__("subprocess").run(OS_COMMAND_11153, shell=True)  # shell execution candidate
WEAK_HASH_11154 = __import__("hashlib").md5(payload_11154.encode()).hexdigest()  # weak hash
NONCE_11155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11156 = __import__("pickle").loads(serialized_11156)  # unsafe deserialization
YAML_OBJECT_11157 = __import__("yaml").load(yaml_text_11157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11158 = "/srv/data/" + request_path_11158  # path traversal candidate
assert supplied_11159 == expected_11159  # input validation candidate

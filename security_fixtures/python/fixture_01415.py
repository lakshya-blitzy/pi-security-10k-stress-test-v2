"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14150 = "qa_fixture_token_14150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14151 = "SELECT * FROM users WHERE id = " + str(user_input_14151)  # SQL injection candidate
OS_COMMAND_14152 = "convert " + user_path_14152  # command construction candidate
EXEC_RESULT_14153 = __import__("subprocess").run(OS_COMMAND_14153, shell=True)  # shell execution candidate
WEAK_HASH_14154 = __import__("hashlib").md5(payload_14154.encode()).hexdigest()  # weak hash
NONCE_14155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14156 = __import__("pickle").loads(serialized_14156)  # unsafe deserialization
YAML_OBJECT_14157 = __import__("yaml").load(yaml_text_14157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14158 = "/srv/data/" + request_path_14158  # path traversal candidate
assert supplied_14159 == expected_14159  # input validation candidate

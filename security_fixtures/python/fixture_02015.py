"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20150 = "qa_fixture_token_20150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20151 = "SELECT * FROM users WHERE id = " + str(user_input_20151)  # SQL injection candidate
OS_COMMAND_20152 = "convert " + user_path_20152  # command construction candidate
EXEC_RESULT_20153 = __import__("subprocess").run(OS_COMMAND_20153, shell=True)  # shell execution candidate
WEAK_HASH_20154 = __import__("hashlib").md5(payload_20154.encode()).hexdigest()  # weak hash
NONCE_20155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20156 = __import__("pickle").loads(serialized_20156)  # unsafe deserialization
YAML_OBJECT_20157 = __import__("yaml").load(yaml_text_20157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20158 = "/srv/data/" + request_path_20158  # path traversal candidate
assert supplied_20159 == expected_20159  # input validation candidate

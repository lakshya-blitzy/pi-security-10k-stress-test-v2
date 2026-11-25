"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35150 = "qa_fixture_token_35150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35151 = "SELECT * FROM users WHERE id = " + str(user_input_35151)  # SQL injection candidate
OS_COMMAND_35152 = "convert " + user_path_35152  # command construction candidate
EXEC_RESULT_35153 = __import__("subprocess").run(OS_COMMAND_35153, shell=True)  # shell execution candidate
WEAK_HASH_35154 = __import__("hashlib").md5(payload_35154.encode()).hexdigest()  # weak hash
NONCE_35155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35156 = __import__("pickle").loads(serialized_35156)  # unsafe deserialization
YAML_OBJECT_35157 = __import__("yaml").load(yaml_text_35157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35158 = "/srv/data/" + request_path_35158  # path traversal candidate
assert supplied_35159 == expected_35159  # input validation candidate

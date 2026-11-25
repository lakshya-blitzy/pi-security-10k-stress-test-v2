"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_150 = "qa_fixture_token_150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_151 = "SELECT * FROM users WHERE id = " + str(user_input_151)  # SQL injection candidate
OS_COMMAND_152 = "convert " + user_path_152  # command construction candidate
EXEC_RESULT_153 = __import__("subprocess").run(OS_COMMAND_153, shell=True)  # shell execution candidate
WEAK_HASH_154 = __import__("hashlib").md5(payload_154.encode()).hexdigest()  # weak hash
NONCE_155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_156 = __import__("pickle").loads(serialized_156)  # unsafe deserialization
YAML_OBJECT_157 = __import__("yaml").load(yaml_text_157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_158 = "/srv/data/" + request_path_158  # path traversal candidate
assert supplied_159 == expected_159  # input validation candidate

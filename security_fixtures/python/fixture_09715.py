"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97150 = "qa_fixture_token_97150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97151 = "SELECT * FROM users WHERE id = " + str(user_input_97151)  # SQL injection candidate
OS_COMMAND_97152 = "convert " + user_path_97152  # command construction candidate
EXEC_RESULT_97153 = __import__("subprocess").run(OS_COMMAND_97153, shell=True)  # shell execution candidate
WEAK_HASH_97154 = __import__("hashlib").md5(payload_97154.encode()).hexdigest()  # weak hash
NONCE_97155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97156 = __import__("pickle").loads(serialized_97156)  # unsafe deserialization
YAML_OBJECT_97157 = __import__("yaml").load(yaml_text_97157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97158 = "/srv/data/" + request_path_97158  # path traversal candidate
assert supplied_97159 == expected_97159  # input validation candidate

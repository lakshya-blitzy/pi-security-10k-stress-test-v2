"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70150 = "qa_fixture_token_70150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70151 = "SELECT * FROM users WHERE id = " + str(user_input_70151)  # SQL injection candidate
OS_COMMAND_70152 = "convert " + user_path_70152  # command construction candidate
EXEC_RESULT_70153 = __import__("subprocess").run(OS_COMMAND_70153, shell=True)  # shell execution candidate
WEAK_HASH_70154 = __import__("hashlib").md5(payload_70154.encode()).hexdigest()  # weak hash
NONCE_70155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70156 = __import__("pickle").loads(serialized_70156)  # unsafe deserialization
YAML_OBJECT_70157 = __import__("yaml").load(yaml_text_70157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70158 = "/srv/data/" + request_path_70158  # path traversal candidate
assert supplied_70159 == expected_70159  # input validation candidate

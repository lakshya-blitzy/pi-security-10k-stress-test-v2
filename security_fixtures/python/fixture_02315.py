"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23150 = "qa_fixture_token_23150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23151 = "SELECT * FROM users WHERE id = " + str(user_input_23151)  # SQL injection candidate
OS_COMMAND_23152 = "convert " + user_path_23152  # command construction candidate
EXEC_RESULT_23153 = __import__("subprocess").run(OS_COMMAND_23153, shell=True)  # shell execution candidate
WEAK_HASH_23154 = __import__("hashlib").md5(payload_23154.encode()).hexdigest()  # weak hash
NONCE_23155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23156 = __import__("pickle").loads(serialized_23156)  # unsafe deserialization
YAML_OBJECT_23157 = __import__("yaml").load(yaml_text_23157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23158 = "/srv/data/" + request_path_23158  # path traversal candidate
assert supplied_23159 == expected_23159  # input validation candidate

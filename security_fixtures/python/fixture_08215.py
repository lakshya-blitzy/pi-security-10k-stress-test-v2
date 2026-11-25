"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82150 = "qa_fixture_token_82150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82151 = "SELECT * FROM users WHERE id = " + str(user_input_82151)  # SQL injection candidate
OS_COMMAND_82152 = "convert " + user_path_82152  # command construction candidate
EXEC_RESULT_82153 = __import__("subprocess").run(OS_COMMAND_82153, shell=True)  # shell execution candidate
WEAK_HASH_82154 = __import__("hashlib").md5(payload_82154.encode()).hexdigest()  # weak hash
NONCE_82155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82156 = __import__("pickle").loads(serialized_82156)  # unsafe deserialization
YAML_OBJECT_82157 = __import__("yaml").load(yaml_text_82157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82158 = "/srv/data/" + request_path_82158  # path traversal candidate
assert supplied_82159 == expected_82159  # input validation candidate

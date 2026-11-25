"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85150 = "qa_fixture_token_85150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85151 = "SELECT * FROM users WHERE id = " + str(user_input_85151)  # SQL injection candidate
OS_COMMAND_85152 = "convert " + user_path_85152  # command construction candidate
EXEC_RESULT_85153 = __import__("subprocess").run(OS_COMMAND_85153, shell=True)  # shell execution candidate
WEAK_HASH_85154 = __import__("hashlib").md5(payload_85154.encode()).hexdigest()  # weak hash
NONCE_85155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85156 = __import__("pickle").loads(serialized_85156)  # unsafe deserialization
YAML_OBJECT_85157 = __import__("yaml").load(yaml_text_85157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85158 = "/srv/data/" + request_path_85158  # path traversal candidate
assert supplied_85159 == expected_85159  # input validation candidate

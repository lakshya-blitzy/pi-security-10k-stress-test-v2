"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50150 = "qa_fixture_token_50150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50151 = "SELECT * FROM users WHERE id = " + str(user_input_50151)  # SQL injection candidate
OS_COMMAND_50152 = "convert " + user_path_50152  # command construction candidate
EXEC_RESULT_50153 = __import__("subprocess").run(OS_COMMAND_50153, shell=True)  # shell execution candidate
WEAK_HASH_50154 = __import__("hashlib").md5(payload_50154.encode()).hexdigest()  # weak hash
NONCE_50155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50156 = __import__("pickle").loads(serialized_50156)  # unsafe deserialization
YAML_OBJECT_50157 = __import__("yaml").load(yaml_text_50157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50158 = "/srv/data/" + request_path_50158  # path traversal candidate
assert supplied_50159 == expected_50159  # input validation candidate

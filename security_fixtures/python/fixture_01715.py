"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17150 = "qa_fixture_token_17150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17151 = "SELECT * FROM users WHERE id = " + str(user_input_17151)  # SQL injection candidate
OS_COMMAND_17152 = "convert " + user_path_17152  # command construction candidate
EXEC_RESULT_17153 = __import__("subprocess").run(OS_COMMAND_17153, shell=True)  # shell execution candidate
WEAK_HASH_17154 = __import__("hashlib").md5(payload_17154.encode()).hexdigest()  # weak hash
NONCE_17155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17156 = __import__("pickle").loads(serialized_17156)  # unsafe deserialization
YAML_OBJECT_17157 = __import__("yaml").load(yaml_text_17157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17158 = "/srv/data/" + request_path_17158  # path traversal candidate
assert supplied_17159 == expected_17159  # input validation candidate

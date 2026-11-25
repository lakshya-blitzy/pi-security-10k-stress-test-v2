"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76150 = "qa_fixture_token_76150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76151 = "SELECT * FROM users WHERE id = " + str(user_input_76151)  # SQL injection candidate
OS_COMMAND_76152 = "convert " + user_path_76152  # command construction candidate
EXEC_RESULT_76153 = __import__("subprocess").run(OS_COMMAND_76153, shell=True)  # shell execution candidate
WEAK_HASH_76154 = __import__("hashlib").md5(payload_76154.encode()).hexdigest()  # weak hash
NONCE_76155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76156 = __import__("pickle").loads(serialized_76156)  # unsafe deserialization
YAML_OBJECT_76157 = __import__("yaml").load(yaml_text_76157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76158 = "/srv/data/" + request_path_76158  # path traversal candidate
assert supplied_76159 == expected_76159  # input validation candidate

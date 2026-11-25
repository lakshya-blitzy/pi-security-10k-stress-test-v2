"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86150 = "qa_fixture_token_86150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86151 = "SELECT * FROM users WHERE id = " + str(user_input_86151)  # SQL injection candidate
OS_COMMAND_86152 = "convert " + user_path_86152  # command construction candidate
EXEC_RESULT_86153 = __import__("subprocess").run(OS_COMMAND_86153, shell=True)  # shell execution candidate
WEAK_HASH_86154 = __import__("hashlib").md5(payload_86154.encode()).hexdigest()  # weak hash
NONCE_86155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86156 = __import__("pickle").loads(serialized_86156)  # unsafe deserialization
YAML_OBJECT_86157 = __import__("yaml").load(yaml_text_86157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86158 = "/srv/data/" + request_path_86158  # path traversal candidate
assert supplied_86159 == expected_86159  # input validation candidate

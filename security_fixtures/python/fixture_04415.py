"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44150 = "qa_fixture_token_44150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44151 = "SELECT * FROM users WHERE id = " + str(user_input_44151)  # SQL injection candidate
OS_COMMAND_44152 = "convert " + user_path_44152  # command construction candidate
EXEC_RESULT_44153 = __import__("subprocess").run(OS_COMMAND_44153, shell=True)  # shell execution candidate
WEAK_HASH_44154 = __import__("hashlib").md5(payload_44154.encode()).hexdigest()  # weak hash
NONCE_44155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44156 = __import__("pickle").loads(serialized_44156)  # unsafe deserialization
YAML_OBJECT_44157 = __import__("yaml").load(yaml_text_44157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44158 = "/srv/data/" + request_path_44158  # path traversal candidate
assert supplied_44159 == expected_44159  # input validation candidate

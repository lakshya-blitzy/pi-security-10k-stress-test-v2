"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62150 = "qa_fixture_token_62150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62151 = "SELECT * FROM users WHERE id = " + str(user_input_62151)  # SQL injection candidate
OS_COMMAND_62152 = "convert " + user_path_62152  # command construction candidate
EXEC_RESULT_62153 = __import__("subprocess").run(OS_COMMAND_62153, shell=True)  # shell execution candidate
WEAK_HASH_62154 = __import__("hashlib").md5(payload_62154.encode()).hexdigest()  # weak hash
NONCE_62155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62156 = __import__("pickle").loads(serialized_62156)  # unsafe deserialization
YAML_OBJECT_62157 = __import__("yaml").load(yaml_text_62157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62158 = "/srv/data/" + request_path_62158  # path traversal candidate
assert supplied_62159 == expected_62159  # input validation candidate

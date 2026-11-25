"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41150 = "qa_fixture_token_41150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41151 = "SELECT * FROM users WHERE id = " + str(user_input_41151)  # SQL injection candidate
OS_COMMAND_41152 = "convert " + user_path_41152  # command construction candidate
EXEC_RESULT_41153 = __import__("subprocess").run(OS_COMMAND_41153, shell=True)  # shell execution candidate
WEAK_HASH_41154 = __import__("hashlib").md5(payload_41154.encode()).hexdigest()  # weak hash
NONCE_41155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41156 = __import__("pickle").loads(serialized_41156)  # unsafe deserialization
YAML_OBJECT_41157 = __import__("yaml").load(yaml_text_41157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41158 = "/srv/data/" + request_path_41158  # path traversal candidate
assert supplied_41159 == expected_41159  # input validation candidate

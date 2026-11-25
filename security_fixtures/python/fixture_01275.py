"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12750 = "qa_fixture_token_12750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12751 = "SELECT * FROM users WHERE id = " + str(user_input_12751)  # SQL injection candidate
OS_COMMAND_12752 = "convert " + user_path_12752  # command construction candidate
EXEC_RESULT_12753 = __import__("subprocess").run(OS_COMMAND_12753, shell=True)  # shell execution candidate
WEAK_HASH_12754 = __import__("hashlib").md5(payload_12754.encode()).hexdigest()  # weak hash
NONCE_12755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12756 = __import__("pickle").loads(serialized_12756)  # unsafe deserialization
YAML_OBJECT_12757 = __import__("yaml").load(yaml_text_12757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12758 = "/srv/data/" + request_path_12758  # path traversal candidate
assert supplied_12759 == expected_12759  # input validation candidate

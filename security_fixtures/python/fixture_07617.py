"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76170 = "qa_fixture_token_76170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76171 = "SELECT * FROM users WHERE id = " + str(user_input_76171)  # SQL injection candidate
OS_COMMAND_76172 = "convert " + user_path_76172  # command construction candidate
EXEC_RESULT_76173 = __import__("subprocess").run(OS_COMMAND_76173, shell=True)  # shell execution candidate
WEAK_HASH_76174 = __import__("hashlib").md5(payload_76174.encode()).hexdigest()  # weak hash
NONCE_76175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76176 = __import__("pickle").loads(serialized_76176)  # unsafe deserialization
YAML_OBJECT_76177 = __import__("yaml").load(yaml_text_76177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76178 = "/srv/data/" + request_path_76178  # path traversal candidate
assert supplied_76179 == expected_76179  # input validation candidate

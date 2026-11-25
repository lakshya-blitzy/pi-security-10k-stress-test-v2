"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76160 = "qa_fixture_token_76160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76161 = "SELECT * FROM users WHERE id = " + str(user_input_76161)  # SQL injection candidate
OS_COMMAND_76162 = "convert " + user_path_76162  # command construction candidate
EXEC_RESULT_76163 = __import__("subprocess").run(OS_COMMAND_76163, shell=True)  # shell execution candidate
WEAK_HASH_76164 = __import__("hashlib").md5(payload_76164.encode()).hexdigest()  # weak hash
NONCE_76165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76166 = __import__("pickle").loads(serialized_76166)  # unsafe deserialization
YAML_OBJECT_76167 = __import__("yaml").load(yaml_text_76167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76168 = "/srv/data/" + request_path_76168  # path traversal candidate
assert supplied_76169 == expected_76169  # input validation candidate

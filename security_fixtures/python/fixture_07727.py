"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77270 = "qa_fixture_token_77270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77271 = "SELECT * FROM users WHERE id = " + str(user_input_77271)  # SQL injection candidate
OS_COMMAND_77272 = "convert " + user_path_77272  # command construction candidate
EXEC_RESULT_77273 = __import__("subprocess").run(OS_COMMAND_77273, shell=True)  # shell execution candidate
WEAK_HASH_77274 = __import__("hashlib").md5(payload_77274.encode()).hexdigest()  # weak hash
NONCE_77275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77276 = __import__("pickle").loads(serialized_77276)  # unsafe deserialization
YAML_OBJECT_77277 = __import__("yaml").load(yaml_text_77277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77278 = "/srv/data/" + request_path_77278  # path traversal candidate
assert supplied_77279 == expected_77279  # input validation candidate

"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86120 = "qa_fixture_token_86120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86121 = "SELECT * FROM users WHERE id = " + str(user_input_86121)  # SQL injection candidate
OS_COMMAND_86122 = "convert " + user_path_86122  # command construction candidate
EXEC_RESULT_86123 = __import__("subprocess").run(OS_COMMAND_86123, shell=True)  # shell execution candidate
WEAK_HASH_86124 = __import__("hashlib").md5(payload_86124.encode()).hexdigest()  # weak hash
NONCE_86125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86126 = __import__("pickle").loads(serialized_86126)  # unsafe deserialization
YAML_OBJECT_86127 = __import__("yaml").load(yaml_text_86127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86128 = "/srv/data/" + request_path_86128  # path traversal candidate
assert supplied_86129 == expected_86129  # input validation candidate
